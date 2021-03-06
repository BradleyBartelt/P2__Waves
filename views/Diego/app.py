""""""
# Flask(__name__) establishes resources on the filesystem (aka package).
# 1. app is control object for flask
# 2. the Flask initializer uses __name__ param to locate root of webserver
# 3. static and templates are of folders that are located relative to directory of Flask execution
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
    return render_template("bradhome.html")

@app.route('/easteregg')
def PythonMiniLab():
    return render_template("Easter_egg.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='127.0.0.1', port='5000')
"""

from flask import render_template, request, Blueprint
from views.Diego.diegominilab import Pi
# from views.Diego import diego_bp
from views.Diego.bubblesort import bubbleSort
diego_bp = Blueprint('diego_bp', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')

@diego_bp.route('/',methods = ["GET","POST"])
def index():
    return render_template("diego/testing.html")

@diego_bp.route('/bubble', methods=["GET", "POST"])
def bubblesort():
    if request.form:
        all_list = []
        b = 1 # to ensure first number is 0

        newbox_counter = request.form.get('newbox_counter')
        print('number of boxes added' +str(newbox_counter))

        numberToItterate = 5
        # iterating through all of the form text fields input
        for i in range(numberToItterate):
            string_used = 'user_input' + str(b)
            user_input = request.form.get(string_used)
            all_list.append(int(user_input))
            b = b + 1

        print(all_list)
        bubble = bubbleSort(all_list)
        return render_template("diego/bubble.html", active_page='Diego', output_list = bubble)

    # conversion = Conversion('', all_list)
    # return render_template("colin/conversion.html", user_input=user_input, conversion=conversion,
    # list_conversion=conversion._list ,active_page='colin', type='multi', type_js=json.dumps('multi'))

    return render_template("diego/bubble.html", active_page='Diego')

# @diego_bp.route('/',methods = ["GET","POST"])
# def index():
#     if request.form:
#         return render_template("diego/dmini_lab.html", pi = Pi(5))
#     return render_template("diego/dmini_lab.html", pi = Pi(5))

# @diego_bp.route('/fibonacci', methods=["GET", "POST"])
# def fibonacci():
#     if request.form:
#         return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))))
#     return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(2))
