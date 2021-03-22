from flask import Blueprint

andrew_bp = Blueprint('andrew', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@andrew_bp.route('/')
def index():
    return "Colin Location"
