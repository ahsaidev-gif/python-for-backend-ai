from fastapi import FastAPI
from ai_project.retrieval.retriever import retrieve_best_chunk

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Assistant API is running"}


@app.get("/ask")
def ask_question(query: str):
    chunks = retrieve_best_chunk(query)

    if chunks:
        return {
            "query": query,
            "answers": chunks
        }

    return {
        "query": query,
        "answer": "No relevant information found"
    }
