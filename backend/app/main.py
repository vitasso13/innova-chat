from fastapi import FastAPI, HTTPException
import contextlib
from app.connectors.pipeline_connector import PipelineConnector
from app.repositories.product_repository import ProductRepository
from app.models.query_model import QueryModel

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    ProductRepository().initialize_database()
    print("Database initialized successfully.")
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/ask")
async def ask_question(query: QueryModel):
    pipline_connector = PipelineConnector(task="question-answering")
    data = ProductRepository().get_products_information()
    context = " ".join([f"{row[1]}: {row[2]}" for row in data if row[2]])

    qa_pipe = {
        'question': query.question,
        'context': context
    }
    answer = pipline_connector.run(pipe=qa_pipe)

    return {'answer': answer['answer']}


@app.post("/product")
async def create_product(id: int, name: str, description: str):
    product_repository = ProductRepository()
    product_repository.insert_product(id, name, description)
    return {'message': 'Product created!'}


