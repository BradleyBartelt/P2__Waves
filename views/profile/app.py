from flask import Blueprint, render_template
from views.profile.models import temp_info
from flask import Blueprint, redirect, render_template, url_for, Flask
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired,Email,Length
from model.module import User, db, user_records
from views.andrew import andrew_bp
from flask_bootstrap import Bootstrap

profile_bp = Blueprint('profile_bp', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=0,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=0,max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(), Length(min=0,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=0,max=80)])

@profile_bp.route('/')
def index():
    return "Colin Location"


@profile_bp.route('/userprofile')
def user_profile():
    return render_template("profile/user_profile.html", list_stories = temp_info.all_stories(), list_post=temp_info.all_post())

@profile_bp.route('/settings')
def user_setting():
    return render_template("profile/settings.html")

@profile_bp.route('/edit')
def user_edit():
    return render_template("profile/edit.html")


@profile_bp.route('/login', methods=["GET", "POST"])
def login():
    #TODO: Make the form accept the User Value, or somehow update the form
    form = LoginForm()
    #TODO Make The SQL Database work

    if form.validate_on_submit():
        #exists = db.session.query(
        #db.session.query(User).filter_by(username='AndrewZhang').exists()
        #).scalar()
        #if exists == True:
        #return "Exists"
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if user.password == form.password.data:
                return '<h1>yay</h1>'

        return '<h1>Invalid username or password</h1>'

    return render_template("profile/login.html", form = form)


@profile_bp.route('/signup',methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        print("I have arrived")
        new_user = User(username = form.username.data, email = form.email.data) #, password = form.password.data
        db.session.add(new_user)
        db.session.commit()
        return '<h1>yay</h1>'

    return render_template("profile/sign_up.html", form = form)

@profile_bp.route('/admin')
def admin():
   return render_template("profile/admin page.html", user_records=user_records)
