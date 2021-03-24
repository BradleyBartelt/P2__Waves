from flask import Blueprint

andrew_bp = Blueprint('andrew_bp', __name__,
                      template_folder='templates',
                      static_folder='static', static_url_path='assets')

from . import app