from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017"

client = MongoClient(mongo_uri)
database = client.market_db
markets_collection = database.markets
