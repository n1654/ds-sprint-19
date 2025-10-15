from model import ModelPredictor

class PredictionService:
    def __init__(self, model_repo, model_name: str):
        self.predictor = ModelPredictor(model_repo, model_name)

    def get_predictions(self, file) -> list:
        data = self.predictor.preprocess_data(file)
        predictions = self.predictor.predict(data)
        results = [{"prediction": pred} for pred in predictions]
        return results

