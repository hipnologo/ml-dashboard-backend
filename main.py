from fastapi import FastAPI
from routers import prediction_router

app = FastAPI()

app.include_router(prediction_router.router, prefix="/api/v1", tags=["predictions"])
