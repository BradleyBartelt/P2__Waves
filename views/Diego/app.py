from flask import Blueprint

diego_bp = Blueprint('diego', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@diego_bp.route('/')
def index():
    return "Diego Location"
