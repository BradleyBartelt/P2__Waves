from flask import Blueprint, render_template
from views.profile.models import temp_info

colin_bp = Blueprint('colin_bp', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@colin_bp.route('/')
def index():
    return render_template('colin/mini_lab.html', active_page='colin')

