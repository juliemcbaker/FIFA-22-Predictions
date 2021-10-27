from typing import Collection
import pymongo
from pymongo import collection
from password import password
import json


conn = f'mongodb+srv://aarvin:{password}@cluster0.j8pgj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(conn)

db = client.fifadb
Collection = db.fifa
Collection.drop()

with open("Resources/FIFA_random_sample.json") as file:
    file_data = json.load(file)

Collection.insert_one(file_data)