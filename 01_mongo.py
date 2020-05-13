import json
import pymongo as pmg
import glob

with open(r'.\keys.json') as f:
    keys = json.load(f)

user = keys['user']
password = keys['password']
public_dns = 'ec2-18-136-123-94.ap-southeast-1.compute.amazonaws.com'
mdb = pmg.MongoClient(
    f'mongodb://{user}:{password}@{public_dns}',
    27017
)

db = mdb['taxonomydb']
col = db['taxonomies']

# List db names.
print(mdb.list_database_names())

file_paths = './documents/*.json'
files = glob.glob(file_paths)

for file in files:
    with open(file) as f:
        file_data = json.load(f)
        x = col.insert_one(file_data)
        print(x.inserted_id)

# Delete documents.
# x = col.delete_many({})
# print(x.deleted_count, "documents deleted.")

# if pymongo >= 3.0 use insert_one() for inserting one document
# collection_currency.insert_one(file_data)
# # if pymongo >= 3.0 use insert_many() for inserting many documents
# collection_currency.insert_many(file_data)

mdb.close()
