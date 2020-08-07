# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

# from flask_mongoalchemy import MongoAlchemy
# import flask_pymongo
# from flask_pymongo import MongoClient

# cluster = MongoClient(mongodb+srv://user:<12345>@cluster0.tbmpc.mongodb.net/<dbname>?retryWrites=true&w=majority)
# cluster = MongoClient(mongo+srv//user,12345@cluster0.tbmpc.mongodb.net/my_mongodb,retryWrites=true&w)
#
# db = cluster["myDatabase"]
# collection = db["table-name"]


from flask_pymongo import PyMongo, MongoClient


CONNECTION_STRING = "mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
# db = client['mb_test']
# users = db["users"]
# requests = db["requests"]
# posts = db["posts"]
db = client.user_applications
posts = db.posts
