from flask import render_template, request
from views.andrew import andrew_bp
from views.andrew.minilab import Pi



@andrew_bp.route('/',methods = ["GET","POST"])
def index():
    if request.form:
        return render_template("mini_lab.html", pi=Pi(int(request.form.get("number"))))
    return render_template("mini_lab.html", pi=Pi(2))


