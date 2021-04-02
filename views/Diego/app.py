from flask import render_template, request
from views.Diego import diego_bp
from views.diegominilab import Phi



@diego_bp.route('/',methods = ["GET","POST"])
def index():
    if request.form:
        return render_template("dmini_lab.html", phi=Phi(int(request.form.get("number"))))
    return render_template("dminilab.html", phi=Phi(2))
