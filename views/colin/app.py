from flask import Blueprint, Flask, render_template, request, redirect, url_for

colin_bp = Blueprint('colin', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@colin_bp.route('/')
def index():
    return "Colin Location"

@colin_bp.route('/userprofile')
def user_profile():
    return render_template("colin/user_profile.html")
