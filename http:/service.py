from fastapi import FastAPI

from model import ClassifyRequest
from ml import MLModel


model: MLModel = None
app = FastAPI()


def init_model(path_to_model, path_to_encoder):
    global model
    model = MLModel(path_to_model, path_to_encoder)


@app.get("/health")
def health_check():
    return {"health": "ok"}


@app.post("/classify")
def classify(request: ClassifyRequest):
    res = model.predict(request)
    return {"result": res[0]}
