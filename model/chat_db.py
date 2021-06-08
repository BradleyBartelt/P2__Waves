from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from model.module import UserChat
import dns

# client = MongoClient("mongodb+srv://test:test@cluster0.qboud.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

USER = "test"
PASSWORD = "test"

client = MongoClient(
    "mongodb+srv://" + USER + ":" + PASSWORD + "@cluster0.qboud.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users_chat")
users_info = chat_db.get_collection("users_info")

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash })

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

mongo_users = []
def user_to_frontend():
    for user in users_collection.find():
        mongo_users.append(user)
user_to_frontend()

if __name__ == "__main__":
    # user_info_create("billy", "billy", "My name is billy and my username is billy", "https://github.com/P5-Tacos/P5-Tacos-thrift-store")
    # user_to_frontend()
    print(mongo_users)