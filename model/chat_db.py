import pymongo
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from model.module import UserChat
from pymongo import ReturnDocument
import dns
import sys
import json
import ssl


# client = MongoClient("mongodb+srv://test:test@cluster0.qboud.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

USER = "test"
PASSWORD = "test"

# client = MongoClient(
#     "mongodb+srv://" + USER + ":" + PASSWORD + "@cluster0.qboud.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

client = pymongo.MongoClient("mongodb+srv://" + USER + ":" + PASSWORD + "@cluster0.qboud.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users_chat")
users_info = chat_db.get_collection("users_info")

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password })

def update_user(user, category,item_of_update):
    users_info.find_one_and_update(
        {"_id": user},
        {"$set": {category:item_of_update }},return_document = ReturnDocument.AFTER)

def get_user(username):
    user_data = users_collection.find_one({'_id': username})
    return UserChat(user_data['_id'], user_data['email'], user_data['password']) if user_data else None

def user_info_create(username, name, bio, link,friend,pfp,posts):
    users_info.insert_one({'_id': username,
                           'name': name,
                           'bio': bio,
                           'website_link': link,
                           'friend':friend,
                           'picture':pfp,
                           'posts':posts
                           })
def get_user_info(username):
    info = users_info.find_one({'_id': username})

    return info

mongo_users = []
def user_to_frontend():
    for user in users_collection.find():
        mongo_users.append(user)
user_to_frontend()

mongo_userz = []
def info_to_frontend():
    for user in users_info.find():
        mongo_userz.append(user)
info_to_frontend()

if __name__ == "__main__":
    #user_info_create("billa", "billy", "My name is billy and my username is billy", "https://github.com/P5-Tacos/P5-Tacos-thrift-store","friend","picture","post")
    #info_to_frontend()
    print(mongo_userz)