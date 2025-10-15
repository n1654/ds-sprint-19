from huggingface_hub import hf_hub_download
import joblib
import pandas as pd
from data_preprocessor import DataPreprocessor

class ModelPredictor:
    def __init__(self, model_repo, model_name: str):
        self.model = self.load_model(model_repo, model_name)

        self.data_preprocessor = DataPreprocessor()

    def load_model(self, model_repo, model_name: str):
        model_file = hf_hub_download(repo_id=model_repo, filename=model_name)
        return joblib.load(model_file)

    def predict(self, data: pd.DataFrame) -> list:
        return self.model.predict(data).tolist()

    def preprocess_data(self, file) -> pd.DataFrame:
        df = self.data_preprocessor.preprocess(file)
        return df

