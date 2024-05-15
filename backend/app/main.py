from fastapi import FastAPI, HTTPException
from backend.app.connectors.pipeline_connector import PipelineConnector
from backend.app.repositories.product_repository import ProductRepository
from backend.app.models.query_model import QueryModel

app = FastAPI()


@app.post("/ask")
async def ask_question(query: QueryModel):
    pipline_connector = PipelineConnector(task="question-answering")
    data = ProductRepository().get_products_information()
    context = " ".join([f"{row[1]}: {row[2]}" for row in data])  # Supondo que a descrição do produto está na segunda coluna

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