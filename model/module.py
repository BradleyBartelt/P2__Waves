from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from model import app
import os

# create a Flask instance
"Setting up the keys are needed for the database"
from flask import Flask, request
import os, json
from flask_migrate import Migrate
from flask_restful import Resource, Api
from sqlalchemy import func
from datetime import datetime
from main import app
from flask_login import UserMixin
from werkzeug.security import check_password_hash

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# Bootstrap(app)
# Bootstrap(app)
db = SQLAlchemy(app)
Migrate(app, db)
api = Api(app)


# api.init_app(app)

# for users stored in mongo DB
class UserChat:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return False

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    def check_password(self, password_input):
        return check_password_hash(self.password, password_input)

# for users stored in sqlite db
class User(db.Model, UserMixin):
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
        self.chat_name = chat_name
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
        self.chatid = chatid
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

    def __init__(self, address, name, phone, description):
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

    def __init__(self, address, name, time, stars, description):
        self.address = address
        self.name = name
        self.phone = time
        self.stars = stars
        self.description = description

    pass


class RatingFood(db.Model):
    __tablename__ = 'RatingFood'

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
        info = {'id': reviews.id, 'restaurant': reviews.restaurant, 'name': reviews.name, 'user': reviews.user,
                'time': str(reviews.time), 'stars': reviews.stars, 'description': reviews.description}
        review_info.append(info)


review_map()


class GetReviewResource(Resource):

    def get(self, id):
        # to decrement the id to ensure that row matches the contents of the list
        review = review_info[int(id) - 1]
        return review

    pass


"Create Database"
"""
json problems with python datatime

https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable/36142844#36142844
"""
class CreateReview(Resource):
    def post(self, restaurant, name, user, stars, description):

        userid = int(db.session.query(func.max(RatingFood.id)).scalar())+1
        print(userid)
        # getting the current time
        now = datetime.now()

        # filling in the data to populate the database
        review = RatingFood(
            id=int(userid),
            restaurant=restaurant,
            name=name,
            user=user,
            time=now,
            stars=int(stars),
            description=str(description)
        )

        reviewJson = json.dumps(review.json(), indent=4, sort_keys=True, default=str)

        print(reviewJson)

        # committing information into the database
        db.session.add(review)
        db.session.commit()

        # adding info into review_info (what is displayed when program asks for allReviews)
        info = {'id': review.id, 'restaurant': review.restaurant, 'name': review.name, 'user': review.user,
                'time': str(review.time), 'stars': review.stars, 'description': review.description}
        review_info.append(info)

        return reviewJson


class AllReviews(Resource):
    def get(self):
          return review_info
    pass


db.create_all()

# information to display on the admin page
user_records = []


  # mapping the front end to the backend, put in the function so we don't have to copy and paste


# mapping the front end to the backend, put in the function so we don't have to copy and paste
def list_user_map():
    user = User.query.all()
    for user in user:
        user_info = {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password}
        user_records.append(user_info)


list_user_map()
