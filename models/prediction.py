from pydantic import BaseModel

class Prediction(BaseModel):
    data: str
    prediction: str
