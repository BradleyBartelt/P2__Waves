from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from model.module import UserChat

client = MongoClient("mongodb+srv://test:test@cluster0.qboud.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users_chat")

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash })

def get_user(username):
    user_data = users_collection.find_one({'_id': username})
    return UserChat(user_data['id'], user_data['email'], user_data['password']) if user_data else None

if __name__ == "__main__":
    print("running chat_db")

    # save_user('andrew','andrew@gmail.com', 'password' )
    # save_user('testing','testing@gmail.com', 'password' )
#
    # print("after creation")