from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.model.model import predict_diagnosis
from app.model.model import __version__ as ver


app = FastAPI(title="Disease Diagnosis", version=ver)

class TextIn(BaseModel):
    text: str


class TextOut(BaseModel):
    disease: str


@app.get("/")
def root():
    return {"message": "Welcome to Disease Diagnosis", "health_check": "OK", "version": ver}


@app.post("/predict", response_model=TextOut)
def predict(text: TextIn):
    disease = predict_diagnosis(text.text)
    return {"disease": disease}