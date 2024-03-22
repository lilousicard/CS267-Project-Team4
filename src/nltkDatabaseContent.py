import os
from pymongo import MongoClient
from nltkParser import words_to_pos_types 

# Retrieve the MongoDB Atlas credentials from environment variables
username = 'lilousicardnoel' 
password = os.getenv('MONGODB_ATLAS_PASSWORD')
if not password:
    raise Exception("MongoDB Atlas password environment variable not set")

# Construct the MongoDB URI
cluster_url = 'cluster0.figrf53.mongodb.net'
db_name = 'newsArticle' 
connection_uri = f"mongodb+srv://{username}:{password}@{cluster_url}/{db_name}?retryWrites=true&w=majority"

# Connect to the MongoDB Atlas cluster
client = MongoClient(connection_uri)
db = client[db_name]

# Open the Articles collection
articles_collection = db['ProQuest-Articles'] 

try:
    # Process each document in the collection
    for article in articles_collection.find():
        # Check if 'wordFamilyContent' field already exists
        if 'wordFamilyContent' in article:
            continue  # Skip this document
        # Extract the content field from the article
        content = article.get('content', '')
        # Process the content through nltkParser to get word families
        word_family_content = words_to_pos_types(content)

        # Update the document with the new field 'wordFamilyContent'
        articles_collection.update_one({'_id': article['_id']}, {'$set': {'wordFamilyContent': word_family_content}})

    print("Processing and updating completed successfully.")
except Exception as e:
    print("An error occurred:", e)
