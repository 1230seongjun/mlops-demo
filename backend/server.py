# server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bs4 import BeautifulSoup
from transformers import pipeline
import requests
import mlflow
import mlflow.transformers

app = FastAPI()

class SummarizeRequest(BaseModel):

    url: str
    model: str
    max_length: int = 150
    min_length: int = 40

# 모델 캐시
MODEL_CACHE = {}


def get_model(model_uri):
    if model_uri not in MODEL_CACHE:
        print(f"Loading model from MLflow: {model_uri}")
        MODEL_CACHE[model_uri] = (
            mlflow.transformers.load_model(model_uri)
        )
        print(model_uri)
        print("Model loaded")
    return MODEL_CACHE[model_uri]

def extract_url(url):
    headers = {
        "User-Agent":"Mozilla/5.0"
    }
    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )
    response.raise_for_status()
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )
    paragraphs = [
        p.get_text(" ", strip=True)
        for p in soup.find_all("p")
    ]
    return "\n".join(paragraphs)

@app.post("/summarize")

def summarize(req: SummarizeRequest):
    try:
        text = extract_url(req.url)
        if len(text) == 0:
            raise HTTPException(
                status_code=400,
                detail="본문을 추출할 수 없습니다."
            )
        summarizer = get_model(req.model)
        result = summarizer(
            text,
            max_length=req.max_length,
            min_length=req.min_length,
            truncation=True
        )
        return {
            "model": req.model,
            "summary": result[0]["summary_text"]
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
