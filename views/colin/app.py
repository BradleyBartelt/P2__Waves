from flask import Blueprint, render_template, request
# from views.profile.models import temp_info
from views.colin.algo.fibonacci import Fibonacci

colin_bp = Blueprint('colin_bp', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@colin_bp.route('/')
def index():
    return render_template('colin/mini_lab.html', active_page='colin')

@colin_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("colin/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))), active_page='colin')
    return render_template("colin/fibonacci.html", fibonacci=Fibonacci(2), active_page='colin')


#<tr><th>Username</th></tr>
#<tr><td><input name="username" type="text" size="20"></td></tr>