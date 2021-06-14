from flask import Blueprint, render_template, request
import requests



crossover_bp = Blueprint('crossover_bp', __name__,
                          template_folder='templates',
                          static_folder='static',
                         static_url_path='assets')

@crossover_bp.route('/')
def index():
    # TODO: need to change out the url for the url on Mr.M's hardware
    url = "http://72.199.26.118:8080/apipull/tweets"

    response = requests.request("GET", url)
    print(response)
    return render_template('crossover/pulling.html', response= response)