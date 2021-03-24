from flask import Blueprint

bradley_bp = Blueprint('bradley', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@bradley_bp.route('/')
def index():
    return "Bradley Location"
