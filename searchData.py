from pymongo import MongoClient

client = MongoClient();
db = client.EnronDB ## our DB is called EnronDB
collection = db.emails ## create a collection within EnronDB called emails

def search(term):
  query = "indexes." + term
  retrieved_docs = collection.find( { query: 1 })
  print("searched docs: ", retrieved_docs.count())
  # print("searched doc #1: ", retrieved_docs[0])

search("heather")