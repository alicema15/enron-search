## This file contains inserting all enron documents into the database.

######## DB SETUP ########

from pymongo import MongoClient
import os

client = MongoClient();
db = client.EnronDB ## our DB is called EnronDB
collection = db.emails ## create a collection within EnronDB called emails

######## INSERT ALL DOCUMENTS FROM ENRON #########

## Inserts documents in batches to mongodb.
## Walks through the directory with all the emails, goes through all subdirectories, and creates
## an object for each file. Stores these files to mongodb in batches of 1000, an arbitrary starting number.
def insert_all_docs(directory):
  all_files = []
  for path, subdirs, files in os.walk(directory):
    if isinstance(files, list):
      for name in files:
          if not name.startswith('.'):
            doc = create_doc(os.path.join(path, name))
            if len(all_files) > 1000:
              try:
                print("inserting: ", len(all_files))
                collection.insert_many(all_files)
                all_files = []
              except:
                all_files = []
                print('error in inserting')
            all_files.append(doc)

## Creates a json format object that mongodb can accept.
## it opens the file at the test site, reads the text, splits all of the text into appropriate indexes
## including prefix strings, and returns this object.
## Sometimes, you can't read the file and this throws an error.
##
## TO-DO: investigate why you can't read the file sometimes.
def create_doc(file_path):
  with open(file_path) as f: ## opens the file
    try:
      text = f.read()

      indexes = split_text(text)
      file_document = {"file_path": file_path, "text": text, "indexes": indexes}
      return file_document
    except:
      print('error')

######## HELPER FUNCTIONS ########

## splits text into a dictionary containing all indexes: words and prefixes.
def split_text(text):
  words_in_text = {}
  word = ""
  for c in text:
    if (c.isalpha()): # checks if the character is a letter. This is how we define a word.
      word = word + c
      if (word not in words_in_text): ## check if the characters are already indexed
        words_in_text[word] = 1
    else:
      word = ""
  return words_in_text

### RUN COMMANDS ####

insert_all_docs('./maildir')


