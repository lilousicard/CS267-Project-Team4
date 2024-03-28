import os
from mongo_utils import get_mongo_client

username = 'lilousicardnoel'
cluster_url = 'cluster0.figrf53.mongodb.net'
db_name = 'newsArticle'
file_path = 'articleTopics.txt'

def store_lines_in_mongodb():
    client = get_mongo_client(username, cluster_url, db_name)
    db = client[db_name]
    collection = db['topicsForAI']
    with open(file_path, 'r') as file:
        for line in file:
            document = {
                "line": line.strip(),  # Remove leading/trailing whitespace
                "has_been_generated": False
            }
            collection.insert_one(document)

    print("All lines have been stored in MongoDB.")

if __name__ == "__main__":
    store_lines_in_mongodb()
