from pymongo import MongoClient

MONGO_URI = "mongodb://root:root@localhost:27017/ai-service?authSource=admin"

client = MongoClient(MONGO_URI)

db = client["ai-service"]

articles = db["articles"]