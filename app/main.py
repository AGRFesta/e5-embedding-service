from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
import os

app = FastAPI()

MODEL_PATH = os.getenv("MODEL_PATH", "e5_model")
model = SentenceTransformer(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

class TextRequest(BaseModel):
    sentences: list[str]
    mode: str = "query"  # "query" oppure "passage"

@app.post("/embed")
def embed(req: TextRequest):
    mode = req.mode.lower()
    if mode not in {"query", "passage"}:
        return {"error": "mode must be 'query' or 'passage'"}
    inputs = [f"{mode}: {s}" for s in req.sentences]
    vectors = model.encode(inputs, normalize_embeddings=True)
    return {"vectors": vectors.tolist()}

@app.post("/count-tokens")
def count_tokens(req: TextRequest):
    mode = req.mode.lower()
    if mode not in {"query", "passage"}:
        return {"error": "mode must be 'query' or 'passage'"}
    counts = []
    for s in req.sentences:
        prefixed = f"{mode}: {s}"
        tokens = tokenizer(prefixed, return_tensors="pt")
        count = tokens['input_ids'].shape[1]
        counts.append({"sentence": s, "token_count": count})
    return {"token_counts": counts}

