from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db = client.todo_db
collection_name = db.get_collection("todo_collection")
