from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.post("/")
async def ask_question(query):
    try:
        print("Question:", query.question)

        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))