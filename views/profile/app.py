from flask import Blueprint, render_template
from views.profile.models import temp_info

profile_bp = Blueprint('profile_bp', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@profile_bp.route('/')
def index():
    return "Colin Location"


@profile_bp.route('/userprofile')
def user_profile():
    return render_template("profile/user_profile.html", list_stories = temp_info.all_stories(), list_post=temp_info.all_post())

@profile_bp.route('/settings')
def user_setting():
    return render_template("profile/settings.html")

@profile_bp.route('/edit')
def user_edit():
    return render_template("profile/edit.html")
