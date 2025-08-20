from pymongo import MongoClient
import os

# MONGO_URI = "mongodb://root:root@localhost:27017/ai-service?authSource=admin"
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://root:root@mongodb:27017/ai-service?authSource=admin")


client = MongoClient(MONGO_URI)

db = client["ai-service"]

articles = db["articles"]