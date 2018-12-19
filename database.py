# coding:utf8
from pymongo import MongoClient
from config import MONGODB_HOST, MONGODB_PORT, MONGODB_USER, MONGODB_PASSWORD, DB_NAME

client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT, connect=False, maxPoolSize=200)
db = client.get_database(DB_NAME)

db.authenticate(MONGODB_USER, MONGODB_PASSWORD)