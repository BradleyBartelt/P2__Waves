from flask import Blueprint, render_template, request
from views.Bradley.binary import Binaryclass
from views.Bradley.bubblesorter import Listerclass

bradley_bp = Blueprint('bradley_bp', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')

@bradley_bp.route('/')
def index():
    return render_template("bradhome.html")

@bradley_bp.route('/minilabB',methods = ["GET","POST"])
def minilabB():
    if request.form:
        return render_template("minilabB.html", binaryclass=Binaryclass(int(request.form.get("input"))))
    return render_template("minilabB.html", binaryclass=Binaryclass(2))

@bradley_bp.route('/bubblesorter',methods = ["GET","POST"])
def bubblesorter():
    inputlist = [1,0]
    if request.form:
        return render_template("bubbles.html", listerclass=Listerclass(request.form.get("input").split(" ")))
    return render_template("bubbles.html", listerclass=Listerclass(inputlist))

