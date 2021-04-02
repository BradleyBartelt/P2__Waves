from flask import Blueprint, render_template, request
from views.Bradley.binary import Binaryclass

bradley_bp = Blueprint('bradley_bp', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@bradley_bp.route('/')
def index():
    if request.form:
        return render_template("minilabB.html", binaryclass=Binaryclass(int(request.form.get("input"))))
    return render_template("minilabB.html", binaryclass=Binaryclass(2))

