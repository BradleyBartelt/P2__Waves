from flask import Blueprint, render_template
from views.colin.models import temp_info

colin_bp = Blueprint('colin', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@colin_bp.route('/')
def index():
    return "Colin Location"


@colin_bp.route('/userprofile')
def user_profile():
    return render_template("colin/user_profile.html", list_stories = temp_info.all_stories(), list_post=temp_info.all_post())
