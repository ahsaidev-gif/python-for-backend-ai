from fastapi import FastAPI
from ai_project.retrieval.retriever import retrieve_best_chunk

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Assistant API is running"}


@app.get("/ask")
def ask_question(query: str):
    chunk = retrieve_best_chunk(query)

    if chunk:
        return {
            "query": query,
            "answer": chunk
        }

    return {
        "query": query,
        "answer": "No relevant information found"
    }
