from pymongo import MongoClient

client = MongoClient();
db = client.EnronDB ## our DB is called EnronDB
collection = db.emails ## create a collection within EnronDB called emails

def retrieve_all_docs():
  retrieved_docs = collection.find( { })
  print("retrieved docs: ", retrieved_docs.count())
  # print("searched doc #1: ", retrieved_docs[0])

retrieve_all_docs()