## This file contains inserting and deleting documents into the database as functions.

from pymongo import MongoClient

client = MongoClient();
db = client.EnronDB ## our DB is called EnronDB
collection = db.emails ## create a collection within EnronDB called emails

### INSERT DOCUMENT ###
test_file_path = 'maildir/allen-p/inbox/1.'
f = open(test_file_path) ## opens a test file
text = f.read()

def insert_doc(file_path, text):
  file_document = {"file_path": file_path, "text": text}
  print("text is here: ", text)
  collection.insert(file_document)

insert_doc(test_file_path, text)

### RETRIEVE DOCUMENT ###


def retrieve_doc(file_path):
  retrieved_doc = collection.find_one({"file_path": file_path})
  print("retrieved doc: ", retrieved_doc)

retrieve_doc(test_file_path)
## TO-DO: Retrieval of the document is working but need to make sure that 
## newlines aren't stored in such a weird way