from fastapi import FastAPI, HTTPException
import contextlib
from app.connectors.pipeline_connector import PipelineConnector
from app.connectors.gemini_connector import GeminiConnector
from app.repositories.product_repository import ProductRepository
from app.models.query_model import QueryModel
from fastapi.middleware.cors import CORSMiddleware


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    ProductRepository().initialize_database()
    print("Database initialized successfully.")
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_question(query: QueryModel):
    pipline_connector = PipelineConnector(task="question-answering")
    data = ProductRepository().get_products_information()
    try:
        context = ""
        for row in data:
            if any(word.lower() in query.question.lower() for word in row[1].split()):
                context += f"{row[1]}: {row[2]} Features: {row[3]} Use Cases: {row[4]} FAQs: {row[5]} "

        # Fallback to full context if no keywords matched
        if not context.strip():
            context = " ".join([f"{row[1]}: {row[2]} Features: {row[3]} Use Cases: {row[4]} FAQs: {row[5]}" for row in data])

        qa_pipe = {
            'question': query.question,
            'context': context.strip()
        }
        # Use o pipeline para perguntar
        answer = pipline_connector.run(pipe=qa_pipe)
         

        return {'answer': answer['answer']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/gemini_ask")
async def ask_question_gemini(query: QueryModel):
    gemini_connector = GeminiConnector()
    try:
        answer = gemini_connector.start_chat(query.question)
        return {'answer': answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/product")
async def create_product(id: int, name: str, description: str):
    product_repository = ProductRepository()
    product_repository.insert_product(id, name, description)
    return {'message': 'Product created!'}


