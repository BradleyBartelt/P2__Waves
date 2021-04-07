from flask import render_template, request
# from views.Diego import diego_bp


"""
@diego_bp.route('/',methods = ["GET","POST"])
def index():
    if request.form:
        return render_template("dmini_lab.html")
    return render_template("dminilab.html")
"""

from flask import render_template, request, Blueprint
# from views.Diego import diego_bp

diego_bp = Blueprint('diego', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@diego_bp.route('/',methods = ["GET","POST"])
def index():
    if request.form:
        return render_template("dmini_lab.html")
    return render_template("dminilab.html")

@diego_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))))
    return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(2))