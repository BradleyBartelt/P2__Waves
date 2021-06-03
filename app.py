"""
Flask(__name__) establishes resources on the filesystem (aka package).
1. app is control object for flask
2. the Flask initializer uses __name__ param to locate root of webserver
3. static and templates are of folders that are located relative to directory of Flask execution
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room
from flask_login import current_user, LoginManager, login_user, login_required, logout_user
import datetime

from views.Bradley.app import bradley_bp
from views.Diego.app import diego_bp
from views.andrew.app import andrew_bp
from views.profile.app import profile_bp
from views.colin.app import colin_bp
from views.Dk.app import dk_bp
from flask_bootstrap import Bootstrap

from model.module import Api
from model.module import GetReviewResource, AllReviews, CreateReview
from main import app
from pizzacompare import Pizzatest
import json
app.register_blueprint(andrew_bp, url_prefix='/andrew')
app.register_blueprint(diego_bp, url_prefix='/diego')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(bradley_bp, url_prefix='/bradley')
app.register_blueprint(colin_bp, url_prefix='/colin')
app.register_blueprint(dk_bp, url_prefix='/dk')

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
bootstrap = Bootstrap(app)

api = Api(app)
api.add_resource(GetReviewResource, '/Food', '/Food/<string:id>')

api.add_resource(
    CreateReview,
    '/createReview',
    '/createReview/<string:restaurant>/<string:name>/<string:user>/<string:stars>/<string:description>'
)

api.add_resource(AllReviews, '/AllFood')

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/easteregg')
def PythonMiniLab():
    return render_template("Easter_egg.html")

@app.route("/chatIndex")
def chatIndex():
    return render_template('chat/chat_index.html')
scroll_poss = 0
@app.route("/PizzaPrices",methods = ["GET","POST"])
def pizzaprices():
    if request.form:
        scroll_poss = request.form['scroll_poss']
        print(scroll_poss)
        return render_template("pizzapi.html", pizzatest=Pizzatest(request.form.get("pizza1"), request.form.get("pizza2")), window_y_value=json.dumps(scroll_poss))
    return render_template("pizzapi.html", pizzatest=Pizzatest("",""))


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/chat")
def chat():

    room = request.args.get("room")
    if room:
        return render_template('chat/chat.html', username=current_user.username, room=room)
    else:
        return redirect('/chatIndex')

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'],
                                                       data['room'],
                                                       data['message']))
    # ensure message in corresponding room
    socketio.emit('receive_message', data, room=data['room'])

@socketio.on('join_room')
def handle_join_room_event(data):
    # saving the time that joined the room
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])

@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])



if __name__ == "__main__":
    # runs the application on the repl development server
    socketio.run(app, debug=True, host='127.0.0.1', port='5000')
