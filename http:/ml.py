import numpy as np
import lightgbm
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from model import ClassifyRequest


class MLModel:
    def __init__(self, path_to_model, path_to_encoder):
        self.model = lightgbm.Booster(model_file=path_to_model)
        self.encoder = LabelEncoder()
        self.encoder.classes_ = np.load(path_to_encoder)

    def preprocess(self, x: ClassifyRequest):
        return np.array([
            x.card_1,
            x.card_2,
            x.addr_1,
            x.transaction_amt,
            x.d15,
            x.day,
            self.encoder.transform(np.array([x.p_email_domain]))[0],
            x.c1,
            x.car_d5,
            x.d2,
            x.hour,
            x.month,
            x.v313,
            x.dow
        ]).reshape(-1, 14)

    def predict(self, data: ClassifyRequest):
        x = self.preprocess(data)
        result = self.model.predict(x)
        return result
