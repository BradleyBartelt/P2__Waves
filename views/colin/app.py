from flask import Blueprint

colin_bp = Blueprint('colin', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@colin_bp.route('/')
def index():
    return "Colin Location"
