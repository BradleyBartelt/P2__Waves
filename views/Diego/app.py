from flask import render_template, request
from views.Diego import diego_bp




@diego_bp.route('/',methods = ["GET","POST"])
def index():
    if request.form:
        return render_template("dmini_lab.html")
    return render_template("dminilab.html")
