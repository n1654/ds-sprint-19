from model import ModelPredictor
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

class PredictionService:
    def __init__(self, model_repo, model_name: str):
        self.predictor = ModelPredictor(model_repo, model_name)

    def get_predictions(self, file) -> list:
        # data             = self.predictor.preprocess_data(file)
        # data_transformed = self.predictor.transform(file)
        predictions      = self.predictor.predict(file)
        results          = [{"prediction": pred} for pred in predictions]
        return results

