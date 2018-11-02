## Use this doc to delete all data from the DB.

from pymongo import MongoClient

client = MongoClient();

db = client.EnronDB ## our DB is called EnronDB
collection = db.emails ## create a collection within EnronDB called emails

### DELETE ALL ITEMS ###

def delete_all_docs():
  x = collection.delete_many({})
  print(x.deleted_count, " documents deleted.")

delete_all_docs()