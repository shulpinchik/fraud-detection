import uvicorn

from service import app, init_model


PATH_TO_MODEL = "ml/fraud_short_model"
PATH_TO_ENCODER = "ml/encoder_short.npy"


if __name__ == '__main__':
    init_model(PATH_TO_MODEL, PATH_TO_ENCODER)
    uvicorn.run(app, host="0.0.0.0", port=8000)