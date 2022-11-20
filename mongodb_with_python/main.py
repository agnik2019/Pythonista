from dotenv import load_dotenv, find_dotenv
import os
import pprint  
import urllib.parse
from pymongo import MongoClient


load_dotenv(find_dotenv())

password = urllib.parse.quote_plus(os.environ.get("MONGODB_PWD"))


connection_string = f"mongodb+srv://agnik:{password}@tutorial.abnybmt.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)


dbs = client.list_database_names()
print(dbs)
# test_db = client.test
# collections = test_db.list_collection_names()
# print(collections)


# def insert_test_doc():
#     collection = test_db.test
#     test_document = {
#         "name":"Agnik",
#         "type": "Test"
#     }
#     inserted_id = collection.insert_one(test_document).inserted_id
#     print(inserted_id)

# insert_test_doc()

# production = client.production
# person_collection = production.person_collection