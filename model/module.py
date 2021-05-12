from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os, json
from flask_migrate import Migrate
from flask_restful import Resource, Api

# create a Flask instance
"Setting up the keys are needed for the database"
app = Flask(__name__)

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Bootstrap(app)
db = SQLAlchemy(app)
Migrate(app,db)
api = Api(app)
#api.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    bio = db.Column(db.String(1000))
    saved_posts = db.Column(db.String(1000))
    setting = db.Column(db.String(1000))

    def __init__(self, username, bio, saved_posts, setting):
        self.username = username
        self.bio = bio
        self.saved_posts = saved_posts
        self.setting = setting

    pass

class GroupChat(db.Model):
    id = db.Column('dm_id', db.Integer, primary_key=True)
    users = db.Column(db.String(100))
    time = db.Column(db.DateTime)
    chat_name = db.Column(db.String(1000))
    description = db.Column(db.String(1000))


    def __init__(self, users, chat_name, time, description):
        self.users = users
        self.chat_name= chat_name
        self.time = time
        self.description = description
    pass

class Dm(db.Model):
    id = db.Column('dm_id', db.Integer, primary_key=True)
    chatid = db.Column(db.Integer)
    username = db.Column(db.String(100))
    time = db.Column(db.DateTime)
    content = db.Column(db.String(1000))


    def __init__(self, chatid, username, time, content):
        self.username = username
        self.chatid= chatid
        self.username = username
        self.time = time
        self.content = content
    pass



class Posts(db.Model):
    id = db.Column('post_id', db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    tags = db.Column(db.String(1000))
    likes = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    location = db.Column(db.String(1000))



    def __init__(self, username, tags, likes, time):
        self.username = username
        self.tags = tags
        self.likes = likes
        self.time = time
    pass

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    phone = db.Column(db.Integer)
    description = db.Column(db.String(1000))

    def __init__(self,address, name, phone, description):
        self.address = address
        self.name = name
        self.phone = phone
        self.description = description

    pass

class RatingLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    time = db.Column(db.DateTime)
    stars = db.Column(db.Float(10))
    description = db.Column(db.String(1000))

    def __init__(self,address, name, time, stars, description):
        self.address = address
        self.name = name
        self.phone = time
        self.stars= stars
        self.description = description

    pass

class RatingFood(db.Model):

    __tablename__= 'RatingFood'

    id = db.Column(db.Integer, primary_key=True)
    restaurant = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    user = db.Column(db.String(100))
    time = db.Column(db.DateTime)
    stars = db.Column(db.Float(10))
    description = db.Column(db.String(1000))

    def __init__(self, id, restaurant, name, user, time, stars, description):
        self.id = id
        self.restaurant = restaurant
        self.name = name
        self.user = user
        self.time = time
        self.stars = stars
        self.description = description

    def json(self):
        return {
            "id": self.id,
            "restaurant": self.restaurant,
            "name": self.name,
            "user": self.user,
            "time": self.time,
            "stars": self.stars,
            "description": self.description
        }

    @property
    def returnJson(self):
        return self.json(self.id)

review_info = []
# mapping the backend to the frontend
def review_map():
    ratings = RatingFood.query.all()
    for reviews in ratings:
        # id, restaurant, name, user, time, stars, description
        info = {'id': reviews.id, 'restaurant': reviews.restaurant, 'name': reviews.name, 'user': reviews.user, 'time': reviews.time, 'stars': reviews.stars, 'description': reviews.description}
        review_info.append(info)

review_map()
class GetReviewResource(Resource):

    # remapping the front end each time a get request is sent
    review_info = []
    def review_map_embbed(self):
        ratings = RatingFood.query.all()
        for reviews in ratings:
            # id, restaurant, name, user, time, stars, description
            info = {
                'id': reviews.id,
                'restaurant': reviews.restaurant,
                'name': reviews.name,
                'user': reviews.user,
                'time': reviews.time,
                'stars': reviews.stars,
                'description': reviews.description
                    }
            review_info.append(info)

    def get(self, id):
        # to decrement the id to ensure that row matches the contents of the list
        review = review_info[int(id)-1]
        # converting to json
        jsonStr = json.dumps(review)
        return jsonStr
    pass

class AllReviews(Resource):
    def get(self):
        review = RatingFood.query.all()

        return [peep.json() for peep in review]
    pass

db.create_all()

# information to display on the admin page
user_records = []
def list_user_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    user = User.query.all()
    for user in user:
        user_info = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password}
        user_records.append(user_info)
list_user_map()

