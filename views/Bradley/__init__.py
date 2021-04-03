from flask import Blueprint

bradley_bp = Blueprint('bradley_bp', __name__,
                      template_folder='templates',
                      static_folder='static', static_url_path='assets')

from . import app