from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import os

app = FastAPI()

# Percorso al modello (default: cartella locale "e5_model")
MODEL_PATH = os.getenv("MODEL_PATH", "e5_model")
model = SentenceTransformer(MODEL_PATH)

class TextRequest(BaseModel):
    sentences: list[str]

@app.post("/embed")
def embed(req: TextRequest):
    inputs = [f"query: {s}" for s in req.sentences]
    vectors = model.encode(inputs, normalize_embeddings=True)
    return {"vectors": vectors.tolist()}
