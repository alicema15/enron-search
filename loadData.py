from pymongo import MongoClient

client = MongoClient();
db = client.EnronDB ## our DB is called EnronDB
collection = db.emails ## create a collection within EnronDB called emails

### INSERT DOCUMENT ###

f = open('maildir/allen-p/inbox/1.') ## opens a test file
text = f.read()

print("text is here: ", text)

file_document = {"username": "allen-p", "text": text}
collection.insert(file_document)

### RETRIEVE DOCUMENT ###

retrieved_doc = collection.find_one({"username": "allen-p"}) 
## TO-DO: Retrieval of the document is working but need to make sure that 
## newlines aren't stored in such a weird way

print("retrieved doc: ", retrieved_doc)