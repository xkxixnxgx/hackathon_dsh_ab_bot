from pymongo import MongoClient
import crypt

# Mongo
db_link = "mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority"
client = MongoClient(db_link)

# База данных
db = client.user_applications

posts = db.posts

def write_data(data: dict):
    encrypted_data = crypt.encrypt_dict(data)
    return posts.insert_one(encrypted_data).inserted_id

def get_data(chat_id) -> list:
    decrypted_data = crypt.decrypt_dict(posts.find({'chat_id': chat_id}))
    return list(decrypted_data)
