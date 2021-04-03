from flask import Blueprint, render_template, request
# from views.profile.models import temp_info
from views.colin.algo.fibonacci import Fibonacci
from views.colin.algo.conversion import Conversion

colin_bp = Blueprint('colin_bp', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@colin_bp.route('/')
def index():
    return render_template('colin/mini_lab_landing.html', active_page='colin')

@colin_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("colin/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))), active_page='colin')
    return render_template("colin/fibonacci.html", fibonacci=Fibonacci(2), active_page='colin')

@colin_bp.route('/conversion', methods=["GET", "POST"])
def conversion():

    # when there is a user input within the code
    if request.form:
        user_input = request.form.get('user_input')
        conversion = Conversion(user_input, [1,2,3,4,5,6,7,8])
        return render_template("colin/conversion.html", user_input=user_input, conversion=conversion, list_conversion=conversion._list ,active_page='colin')
    # default configuration
    conversion = Conversion(0, [1,2,3,4,5,6,7,8])
    return render_template("colin/conversion.html", conversion=conversion, list_conversion=conversion._list ,active_page='colin')


#<tr><th>Username</th></tr>
#<tr><td><input name="username" type="text" size="20"></td></tr>