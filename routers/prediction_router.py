from fastapi import APIRouter
from models.prediction import Prediction
from database import mongodb, redisdb
import json

router = APIRouter()

@router.post("/predict")
async def predict_data(payload: Prediction):
    # Mock ML prediction logic
    prediction_result = payload.data[::-1]  # Just reversing string for now

    # Save prediction and data to MongoDB
    mongodb.prediction_collection.insert_one({"data": payload.data, "prediction": prediction_result})

    # Cache prediction to Redis
    redisdb.redis_client.set(payload.data, prediction_result)

    return {"prediction": prediction_result}

@router.get("/predictions/history")
async def get_prediction_history():
    # Fetch predictions from MongoDB
    predictions = list(mongodb.prediction_collection.find({}))
    return {"predictions": predictions}
