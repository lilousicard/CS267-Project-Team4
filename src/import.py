from pymongo import MongoClient
import json

# Replace the following variables with your specific information
uri = "mongodb+srv://lilousicardnoel:XqU39QzO0LbKab9G@cluster0.figrf53.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
database_name = "newsArticle"
collection_name = "articles"
json_file_path = "parsed_articles2.json"

try:
    # Establish a connection to the MongoDB Atlas cluster
    client = MongoClient(uri)

    # Select the database and collection
    db = client[database_name]
    collection = db[collection_name]

    # Load the JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Check if data is a list of documents or a single document
    if isinstance(data, list):
        # Insert multiple documents if it's a list
        collection.insert_many(data)
        print(f"Inserted {len(data)} documents.")
    else:
        # Insert a single document if it's not a list
        collection.insert_one(data)
        print("Inserted one document.")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the connection
client.close()

