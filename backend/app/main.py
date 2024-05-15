from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

DATABASE = 'database.db'

class QueryModel(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: QueryModel):

    answer = {
        'answer': 'Não foi possível encontrar uma resposta.'
    }

    return {'answer': answer['answer']}