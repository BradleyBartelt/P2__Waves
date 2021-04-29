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
@dk_bp.route('/testing')
def testing():
    return render_template('Dk/testing.html', active_page='Dk')
@dk_bp.route('/bubbles0rt')
def bubblesort():
    return render_template('Dk/bubbles0rt.html', active_page='Dk')