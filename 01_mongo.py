import json
import pymongo as pmg

mdb = pmg.MongoClient(
    'ec2-18-136-123-94.ap-southeast-1.compute.amazonaws.com',
    27017,
    ssl=True,
    ssl_keyfile='./plantx.pem'
)

db = mdb['taxonomydb']
col = db['taxonomies']

with open('./documents/Apache_HTTPS_taxonomy.json') as f:
    file_data = json.load(f)

x = col.insert_one(file_data)

print(x.inserted_id)


# if pymongo >= 3.0 use insert_one() for inserting one document
# collection_currency.insert_one(file_data)
# # if pymongo >= 3.0 use insert_many() for inserting many documents
# collection_currency.insert_many(file_data)

mdb.close()
