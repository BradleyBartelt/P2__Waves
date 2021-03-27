from flask import Blueprint, redirect, render_template, url_for, Flask
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired,Email,Length
from model.module import User,db
from views.andrew import andrew_bp
from flask_bootstrap import Bootstrap



app = Flask(__name__)
db.init_app(app)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=0,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=0,max=80)])
    remember = BooleanField('remember me')



class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(), Length(min=0,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=0,max=80)])


@andrew_bp.route('/')
def index():
    return render_template('mini_lab.html')

@andrew_bp.route('/login', methods=["GET", "POST"])
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

    return render_template("login.html", form = form)


@andrew_bp.route('/signup',methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>yay</h1>'

    return render_template("sign_up.html", form = form)

