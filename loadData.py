## This file contains inserting and deleting documents into the database as functions.

######## DB SETUP ########

from pymongo import MongoClient

client = MongoClient();
db = client.EnronDB ## our DB is called EnronDB
collection = db.emails ## create a collection within EnronDB called emails
## TO-DO: text key too large to index
# collection.create_index("file_path")

######## DB QUERY FUNCTIONS ########

### INSERT DOCUMENT ###
test_file_path = 'maildir/allen-p/inbox/1.'
f = open(test_file_path) ## opens a test file
text = f.read()

def insert_doc(file_path, text):
  indexes = split_text(text)
  file_document = {"file_path": file_path, "text": text, "indexes": indexes}
  # print("text is here: ", text)
  collection.insert(file_document)

insert_doc(test_file_path, text)

### RETRIEVE DOCUMENT ###

def retrieve_doc(file_path):
  retrieved_doc = collection.find_one({"file_path": file_path})
retrieve_doc(test_file_path)
## TO-DO: Retrieval of the document is working but need to make sure that 
## newlines aren't stored in such a weird way

### RETRIEVE ALL DOCUMENTS ###

def retrieve_all_docs():
  retrieved_docs = collection.find( {} )
  print("All docs: ", retrieved_docs.count())

retrieve_all_docs() ## verified that it keeps inserting redundent files into the DB correctly across many instances

### SEARCH ###
## Right now, just searches by seeing if the index for the word exists in the document ##
## TO-DO: Support multi-word searches ##
def search(term):
  query = "indexes." + term
  retrieved_docs = collection.find( { query: 1 })
  print("searched docs: ", retrieved_docs.count())
  print("searched doc #1: ", retrieved_docs[0])

search("heather")
##def insert_all_enron_docs(directory):


######## HELPER FUNCTIONS ########

def split_text(text):
  words_in_text = {}
  word = ""
  for c in text:
    if (c.isalpha()):
      word = word + c
    else:
      if len(word)> 0:
        words_in_text[word] = 1
      word = ""
  return words_in_text

