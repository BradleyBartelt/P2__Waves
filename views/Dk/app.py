from flask import Blueprint, render_template, request
# from views.profile.models import temp_info
from views.colin.algo.fibonacci import Fibonacci
from views.colin.algo.conversion import Conversion
import json

dk_bp = Blueprint('dk_bp', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@dk_bp.route('/')
def index():
    return render_template('Dk/mini_lab_landing.html', active_page='Dk')
