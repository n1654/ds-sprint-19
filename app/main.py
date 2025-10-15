import os
import logging
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from io import StringIO
from service import PredictionService

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

model_repo = os.getenv("MODEL_REPO")
model_name = os.getenv("MODEL_NAME")
prediction_service = PredictionService(model_repo, model_name)

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents       = await file.read()
        csv_data       = StringIO(contents.decode("utf-8"))
        processed_data = prediction_service.predictor.preprocess_data(csv_data)
        predictions    = prediction_service.get_predictions(processed_data)
        logger.info("Предсказания выполнены успешно для файла: %s", file.filename)
        return {"predictions": predictions}
    except Exception as e:
        logger.error("Ошибка при обработке файла %s: %s", file.filename, str(e))
        raise HTTPException(status_code=400, detail=f"Ошибка при обработке файла: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

