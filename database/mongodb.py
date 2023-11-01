from pymongo import MongoClient
from decouple import config

client = MongoClient(config('MONGO_URL'))
db = client["ml_dashboard_db"]
prediction_collection = db["predictions"]
