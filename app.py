from fastapi import FastAPI
from pydantic import BaseModel
from ragchunking1 import get_most_relevant_chunk

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Chunking API! Use /get_relevant_chunk to get results."}


class RequestData(BaseModel):
    text: str
    question: str

@app.post("/get_relevant_chunk")
async def get_relevant_chunk(data: RequestData):
    chunk, similarity = get_most_relevant_chunk(data.text, data.question)
    if chunk is None:
        return {"error": "Failed to process the input"}
    return {
        "question": data.question,
        "most_relevant_chunk": chunk,
        "similarity_score": similarity
    }
