from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient

config = dotenv_values(".env")

mongodb_client = MongoClient(config["URI"])
database = mongodb_client["development"]
