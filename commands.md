<!-- make database -->
db = db.getSiblingDB('DATABASE_NAME')

<!-- drop database -->
db.dropDatabase()

<!-- make collection -->
db.createCollection(name, options)

<!-- insert document -->
db.COLLECTION_NAME.insert(document)
