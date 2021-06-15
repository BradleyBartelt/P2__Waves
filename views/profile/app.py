import login as login
from werkzeug.security import check_password_hash

from views.profile.models import temp_info
from flask import Blueprint, redirect, render_template, url_for, request, session
from flask_login import current_user, LoginManager, login_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from model.module import db, user_records, func
from main import app
from views.andrew import andrew_bp
from flask_bootstrap import Bootstrap
from model.chat_db import *
import json, random, requests


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


"""@login_manager.user_loader
def load_user(username):
    for user in mongo_users:
        if user["_id"] == username:
            u = user
            if not u:
                return None
        return User(username=u['_id'])"""


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)

@profile_bp.route('/')
def index():
    return "Colin Location"


@profile_bp.route('/userprofile')
def user_profile():
    """if request.form:
        target = request.form["input"]

        for item in mongo_users:
            if item["_id"] == target:
                find = {"username": item["_d"], "age": 21, "single?": True}
                return (render_template("profile/Search Result.html", find=find, exist=True))"""
    if current_user.is_authenticated:
        info = get_user_info(current_user.username)
        print(info)
        return render_template("profile/user_profile.html", list_stories=temp_info.all_stories(),
                               list_post=info["posts"], info=info)
    # default contents of guest user

    info = {'_id':"guest",
                'name':"guest",
                'bio':"this is the bio of the guest",
                'website_link':"https://github.com/BradleyBartelt/P2__Waves",
                'friend':[],
                'picture':"https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png",
                'posts':[]

                }
    return render_template("profile/user_profile.html", list_stories=temp_info.all_stories(),
                           list_post=info["posts"], info=info)


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
        print("entering in validation")
        #user = User.query.filter_by(username = form.username.data).first()
        for user in mongo_users:
            if user["_id"] == form.username.data:
                if user["password"] == form.password.data:
                    user_obj = User(username = user["_id"])
                    # print(user_obj["username"])
                    # print(user_obj["password"])
                    session['username'] = form.username.data
                    login_user(user_obj)
                    return redirect(url_for('profile_bp.user_profile'))
        #if user:
            #if user.password == form.password.data:
                #login_user(user)
                #return redirect(url_for('profile_bp.user_profile'))

        return '<h1>Invalid username or password</h1>'

    return render_template("profile/login.html", form=form)

# here is the code the corresponds to the press of the button in base
@profile_bp.route('/searched', methods=["GET", "POST"])
def searchresult():
    find = {"username": "Default", "age": 0, "single?": False}
    List = []
    exist = False

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
            print(request.form)
            for user in mongo_userz:
                if user["_id"] == name:
                    previous_search = name
                    print(previous_search)
                    bio = user["bio"]
                    ratings = 0
                    friend = len(user["friend"])
                    post = len(user["posts"])
            return render_template("profile/user_display.html",name = name, bio = bio, post = post, friend = friend, ratings = ratings)

        if form_name == "add":
            name = previous_search
            for user in mongo_userz:
                if user["_id"] == name:
                    user_current = session["username"]
                    for userz in mongo_userz:
                        if userz["_id"] == user_current:

                            New_list1 = userz["friend"].append(user["_id"])
                            New_list2 = user["friend"].append(userz["_id"])
                            update_user(userz["_id"],"friend",New_list1)
                            update_user(user["_id"],"friend",New_list2)
                            print(user)
                            print(userz)
                    bio = user["bio"]
                    ratings = 0
                    friend = len(user["friend"])
                    post = len(user["posts"])
            return render_template("profile/user_display.html",name = name, bio = bio, post = post, friend = friend, ratings = ratings)
    #return render_template("profile/user_display.html",name = name, bio = bio, post = post, friend = friend, ratings = ratings)
@profile_bp.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():

        save_user(form.username.data, form.email.data, form.password.data)
        user_info_create(form.username.data,
                         form.username.data,
                         "this is the default bio",
                         "default website link",
                         [],
                         "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png",
                         []
                         )

        #return '<h1>yay</h1>'
        return redirect(url_for('profile_bp.login')) #userprofile
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

@profile_bp.route('/api_pull')
def api_pull():
    # getting the qunaity of row entries to use for the random selection
    urlList = "https://pieceofthepi.nighthawkcodingsociety.com/AllFood"
    response_list = requests.request("GET", urlList)
    all_list = json.loads(response_list.text)

    # getting a random field from the entire database len(all_list) corresponds to number of rows in database
    url = "https://pieceofthepi.nighthawkcodingsociety.com/Food/" + str(random.randint(1, len(all_list)))
    response = requests.request("GET", url)

    # current the request
    dictionary = response.text
    y = json.loads(dictionary)
    return render_template('profile/api/api_pull.html', data = y)

@profile_bp.route('/api_app_pull')
def api_all_pull():
    # getting the qunaity of row entries to use for the random selection
    urlList = "https://pieceofthepi.nighthawkcodingsociety.com/AllFood"
    response_list = requests.request("GET", urlList)
    all_list = json.loads(response_list.text)

    return render_template('profile/api/api_all_pull.html', data = all_list)

@profile_bp.route('/api_form_POST', methods=["GET", "POST"])
def api_form_POST():
    if request.method == 'POST':
        # getting the information from the form
        restaurant = request.form.get('restaurant')
        name = request.form.get('name')
        star_count = request.form.get("star_count")
        message_input = request.form.get("message")

        # formatting information into the URL use to access the API
        url_info = 'https://pieceofthepi.nighthawkcodingsociety.com/createReview/' + str(restaurant) + "/" + str(name) + "/peasant/" +str(star_count) + '/'+str(message_input)
        print(url_info)

        # POST to the API
        requests.post(url_info)

        # render the default page
        return render_template('profile/api/api_form_POST.html')

    return render_template('profile/api/api_form_POST.html')