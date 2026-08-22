import pymongo

MONGO_DB_URL = "mongodb+srv://rekhahnd5731_db_user:Lochan123@cluster0.cnfiki4.mongodb.net/?appName=Cluster0"

client = pymongo.MongoClient(
    MONGO_DB_URL,
    serverSelectionTimeoutMS=10000
)

client.admin.command("ping")

print("MongoDB connection successful!")

print("\nDatabases:")
for db_name in client.list_database_names():
    print(" -", db_name)

db = client["ARAVNYX"]

print("\nCollections in ARAVNYX:")
for collection_name in db.list_collection_names():
    count = db[collection_name].count_documents({})
    print(f" - {collection_name}: {count} documents")