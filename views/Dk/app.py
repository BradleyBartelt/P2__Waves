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
@dk_bp.route('/bubbles0rt', methods=["GET", "POST"])
def bubblesort():
    if request.form:
        all_list = []
        b = 1 # to ensure first number is 0
#
        #newbox_counter = request.form.get('newbox_counter')
        #print('number of boxes added' +str(newbox_counter))
#
        numberToItterate = 5
        # iterating through all of the form text fields input
        for i in range(numberToItterate):
            string_used = 'user_input' + str(b)
            user_input = request.form.get(string_used)
            all_list.append(int(user_input))
            b = b + 1

       # print(all_list)
        #bubble = BubbleSort(all_list)
        return render_template('Dk/bubbles0rt.html', active_page='Dk', testing=all_list)

    # conversion = Conversion('', all_list)
    # return render_template("colin/conversion.html", user_input=user_input, conversion=conversion,
    # list_conversion=conversion._list ,active_page='colin', type='multi', type_js=json.dumps('multi'))

    return render_template('Dk/bubbles0rt.html', active_page='Dk')
