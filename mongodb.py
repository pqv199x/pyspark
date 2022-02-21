from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'agenda'
COLLECTION_NAME = 'agenda'

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection = connection[DB_NAME][COLLECTION_NAME]
result = collection.find({})
# print(result)
for doc in result:
    print(doc)

# print(result)