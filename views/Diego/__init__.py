from flask import Blueprint

diego_bp = Blueprint('diego_bp', __name__,
                      template_folder='templates',
                      static_folder='static', static_url_path='assets')

from . import app