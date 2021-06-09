import login as login
from werkzeug.security import check_password_hash

from views.profile.models import temp_info
from flask import Blueprint, redirect, render_template, url_for, request, session
from flask_login import current_user, LoginManager, login_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from model.module import User, db, user_records, func
from main import app
from views.andrew import andrew_bp
from flask_bootstrap import Bootstrap
from model.chat_db import *


profile_bp = Blueprint('profile_bp', __name__,
                       template_folder='templates',
                       static_folder='static', static_url_path='assets')

app.secret_key = 'xxxxyyyyyzzzzz'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=0, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=0, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=0, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=0, max=80)])

class User:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)


    @login_manager.user_loader
    def load_user(username):
        for user in mongo_users:
            if user["_id"] == username:
                u = user
                if not u:
                    return None
            return User(username=u['_id'])

"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
"""

@profile_bp.route('/')
def index():
    return "Colin Location"


@profile_bp.route('/userprofile')
def user_profile():
    if request.form:
        target = request.form["input"]

        for item in mongo_users:
            if item["_id"] == target:
                find = {"username": item["_d"], "age": 21, "single?": True}
                return (render_template("profile/Search Result.html", find=find, exist=True))

    return render_template("profile/user_profile.html", list_stories=temp_info.all_stories(),
                           list_post=temp_info.all_post())


@profile_bp.route('/settings')
def user_setting():
    return render_template("profile/settings.html")


@profile_bp.route('/edit')
def user_edit():
    return render_template("profile/edit.html")

@profile_bp.route('/login', methods=["GET", "POST"])
def login():
    # TODO: Make the form accept the User Value, or somehow update the form
    form = LoginForm()
    # TODO: Make The SQL Database work

    if form.validate_on_submit():
        #user = User.query.filter_by(username = form.username.data).first()
        for user in mongo_users:
            if user["_id"] == form.username.data:
                if user["password"] == form.password.data:
                    user_obj = User(username = user["_id"])
                    login_user(user_obj)
                    return redirect(url_for('profile_bp.user_profile'))
        #if user:
            #if user.password == form.password.data:
                #login_user(user)
                #return redirect(url_for('profile_bp.user_profile'))

        return '<h1>Invalid username or password</h1>'

    return render_template("profile/login.html", form=form)


@profile_bp.route('/searched', methods=["GET", "POST"])
def searchresult():
    find = {"username": "Default", "age": 0, "single?": False}
    List = []
    exist = False
    print(user_records)
    if request.form:
        temp_list = []
        for item in mongo_users:
            temp_list.append(item)
        """
        target = request.form["input"]
        print(target)
        for item in user_records:
            if item["username"] == target:
                find = {"username": item["username"], "age": 21, "single?": True}
                return (render_template("profile/Search Result.html", find=find, exist=True))"""
        target = request.form["input"]
        x = 0
        while x < len(target):
            for item in temp_list:
                if item["_id"] == target:
                    if item not in List:
                        List.append(item)
                    exist = True
                if target[0:x+1] in item["_id"]:
                    if item not in List:
                        List.append(item)
                    exist = True
                    #temp_list.pop(temp_list.index(item))
            x = x+1
    return (render_template("profile/Search Result.html", List=List, exist=exist))
    return (render_template("profile/Search Result.html", List=List, exist=exist))
previous_search = "None"
@profile_bp.route('user_display',methods = ["GET","POST"])
def display():
    global previous_search
    name = "Invalid User"
    bio = "This user exists in the old database"
    post = "null user"
    friend = "null user"
    ratings = "null user"
    if request.method == 'POST':
        form_name = request.form['name']
        if form_name == "view":
            name = request.form["username"]
            print("What's the name" + name)
            for user in mongo_userz:
                if user["_id"] == name:
                    previous_search = name
                    print(previous_search)
                    bio = user["bio"]
                    ratings = 0
                    friend = len(user["friend"])
                    post = len(user["posts"])
            return render_template("profile/user_display.html",name = name, bio = bio, post = post, friend = friend, ratings = ratings)

        '''if form_name == "add":
            name = previous_search
            for user in mongo_userz:
                if user["_id"] == name:
                    user_current = session["_id"]
                    for userz in mongo_userz:
                        if userz["_id"] == user_current:
                            New_list1 = userz["friend"].append(user["_id"])
                            New_list2 = user["friend"].append(userz["_id"])
                            update_user(user_current,"friend",New_list1)
                            update_user(user,"friend",New_list2)
                    bio = user["bio"]
                    ratings = 0
                    friend = len(user["friend"])
                    post = len(user["posts"])
            return render_template("profile/user_display.html",name = name, bio = bio, post = post, friend = friend, ratings = ratings)'''
    #return render_template("profile/user_display.html",name = name, bio = bio, post = post, friend = friend, ratings = ratings)
@profile_bp.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        # printing the form information in the terminal
        # print(form.username.data)
        # print(form.email.data)
        # print(form.password.data)

        # getting the id for the new entry
        userid = int(db.session.query(func.max(User.id)).scalar()) + 1

        # adding the form information into the database
        new_user = User(id=userid, username=form.username.data, email=form.email.data,
                        password=form.password.data)  # , password = form.password.data
        db.session.add(new_user)
        db.session.commit()

        return '<h1>yay</h1>'

    return render_template("profile/sign_up.html", form=form)


@profile_bp.route('/admin')
def admin():
    return render_template("profile/admin page.html", user_records=user_records, mongo_users=mongo_users)

@profile_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    print("logging out")
    return redirect(url_for('profile_bp.user_profile'))