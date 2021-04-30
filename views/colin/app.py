from flask import Blueprint, render_template, request
# from views.profile.models import temp_info
from views.colin.algo.fibonacci import Fibonacci
from views.colin.algo.conversion import Conversion
from views.colin.algo.bubble_sort import BubbleSort
from views.colin.algo.bubble_sort2 import BubbleSortString
import json

colin_bp = Blueprint('colin_bp', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@colin_bp.route('/')
def index():
    return render_template('colin/mini_lab_landing.html', active_page='colin')

@colin_bp.route('/template')
def school():
    return render_template('colin/w3school.html', active_page='colin')

@colin_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("colin/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))), active_page='colin')
    return render_template("colin/fibonacci.html", fibonacci=Fibonacci(2), active_page='colin')

@colin_bp.route('/bubblesort', methods=["GET", "POST"])
def bubblesort():
    if request.form:
        all_list = []

        newbox_counter = request.form.get('newbox_counter')
        newbox_counter_string = request.form.get('newbox_counter_string')
        print('number of boxes added' +str(newbox_counter))
        print('number of boxes added string' +str(newbox_counter_string))

        input_type = request.form.get('input_type')
        print(input_type)

        if input_type == 'integer':
            b = 1 # to ensure first number is 0
            numberToItterate = 5 + int(newbox_counter)
            # iterating through all of the form text fields input
            for i in range(numberToItterate):
                string_used = 'user_input' + str(b)
                user_input = request.form.get(string_used)
                print(user_input)
                all_list.append(int(user_input))
                b = b + 1

            print(all_list)
            bubble = BubbleSort(all_list)
        else:
            b = 1 # to ensure first number is 0
            numberToItterate = 5 + int(newbox_counter_string)
            # iterating through all of the form text fields input
            for i in range(numberToItterate):
                string_used = 'user_input_string' + str(b)
                user_input = request.form[string_used]
                print('value of ' + str(string_used) +': '+ str(user_input))
                all_list.append(user_input)
                b = b + 1

            print(all_list)
            bubble = BubbleSortString(all_list)


        return render_template("colin/bubble_sort.html", active_page='colin', output_list = bubble.OuputList)

    # conversion = Conversion('', all_list)
    # return render_template("colin/conversion.html", user_input=user_input, conversion=conversion,
    # list_conversion=conversion._list ,active_page='colin', type='multi', type_js=json.dumps('multi'))

    return render_template("colin/bubble_sort.html", active_page='colin')

# bubble_sort

@colin_bp.route('/conversion', methods=["GET", "POST"])
def conversion():

    # when there is a user input within the code
    if request.form:
        #  getting the input of a single field
        user_input = request.form.get('user_input0')
        print(str(user_input))

        if user_input == None:
            # if the user input was not filled
            all_list = []
            b = 1 # to ensure first number is 0
            for i in range(5):
                string_used = 'user_input' + str(b)
                user_input = request.form.get(string_used)
                all_list.append(int(user_input))
                b = b + 1
            print(all_list)
            conversion = Conversion('', all_list)
            return render_template("colin/conversion.html", user_input=user_input, conversion=conversion,
                                   list_conversion=conversion._list ,active_page='colin', type='multi', type_js=json.dumps('multi'))
        else:
            # if the user input is not zero (it was filled)
            conversion = Conversion(user_input, '')
            return render_template("colin/conversion.html", user_input=user_input, conversion=conversion, active_page='colin',
                                   type='single', type_js=json.dumps('single'))

    # default configuration
    conversion = Conversion(0, [1,2,3,4,5,6,7,8])
    return render_template("colin/conversion.html", conversion=conversion, list_conversion=conversion._list ,active_page='colin')


#<tr><th>Username</th></tr>
#<tr><td><input name="username" type="text" size="20"></td></tr>