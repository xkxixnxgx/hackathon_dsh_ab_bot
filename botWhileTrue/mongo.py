from pymongo import MongoClient

# Mongo
db_link = "mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority"
client = MongoClient(db_link)

# База данных
db = client.user_applications

posts = db.posts

def write_data(data: dict):
    return posts.insert_one(data).inserted_id

def get_data(chat_id) -> list:
    return list(posts.find({'chat_id': chat_id}))