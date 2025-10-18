import pandas as pd
from model import ModelPredictor
from data_preprocessor import DataPreprocessor

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

class PredictionService:
    def __init__(self, model_repo, model_name: str):
        self.predictor    = ModelPredictor(model_repo, model_name)
        self.preprocessor = DataPreprocessor()

    def get_predictions(self, file) -> list:
        predictions      = self.predictor.predict(file)
        return predictions


