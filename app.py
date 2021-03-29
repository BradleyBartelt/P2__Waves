"""
Flask(__name__) establishes resources on the filesystem (aka package).
1. app is control object for flask
2. the Flask initializer uses __name__ param to locate root of webserver
3. static and templates are of folders that are located relative to directory of Flask execution
"""

from flask import Flask, render_template
from flask import Flask

from views.Bradley.app import bradley_bp
from views.Diego.app import diego_bp
from views.andrew.app import andrew_bp
from views.profile.app import profile_bp
from views.colin.app import colin_bp
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.register_blueprint(andrew_bp, url_prefix='/andrew')
app.register_blueprint(diego_bp, url_prefix='/diego')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(bradley_bp, url_prefix='/bradley')
app.register_blueprint(colin_bp, url_prefix='/colin')

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/easteregg')
def PythonMiniLab():
    return render_template("Easter_egg.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='127.0.0.1', port='5000')