from flask import render_template, request
from views.diego import diego_bp
from views.diegominilab import Pi



@diego_bp.route('/',methods = ["GET","POST"])
def index():
    if request.form:
        return render_template("dmini_lab.html", pi=Pi(int(request.form.get("number"))))
    return render_template("dminilab.html", pi=Pi(2))
