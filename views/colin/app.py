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

def create_coord_list():
    # this is taking the information from the input boxes
    all_list = []
    b = 1 # to ensure first number is 0
    for i in range(3):

        # defining precursor id
        string_used_x = 'x_coord' + str(b)
        string_used_y = 'y_coord' + str(b)

        # getting values from form
        user_input_x = request.form.get(string_used_x)
        user_input_y = request.form.get(string_used_y)

        # appending values into list from the form in the order, x coordinate, y coordinate
        all_list.append(int(user_input_x))
        all_list.append(int(user_input_y))
        b = b + 1

    return all_list
def create_string(return_list):
    coord_string = ''
    for i in range(len(return_list)):
        if i > 0:
            coord_string = coord_string+ ","+str(return_list[i])
        else:
            coord_string = coord_string+ str(return_list[i])
    return coord_string

inital_coords = [200,10,250,190,160,210]
inital_string = create_string(inital_coords)

@colin_bp.route('/polygon', methods=["GET", "POST"])
def polygon():
    if request.form:

        return_list = create_coord_list()
        finalString = create_string(return_list)

        listToPass = str(return_list)
        print("list to pass: " +str(listToPass))
        return render_template("colin/college_board_polygon.html", active_page='colin', stringUse = finalString, listToPass = listToPass, numbList=return_list)

    return render_template("colin/college_board_polygon.html", active_page='colin', stringUse= inital_string, numbList = inital_coords )



def translateBy(res, valuex, valuey, reset):
    if reset == 'reset':
        res = inital_coords
    else:
        for i in range(len(res)):
            if i % 2 == 0:
                res[i] = int(res[i]) + int(valuex)
            else:
                res[i] = res[i] - int(valuey)
    return res



@colin_bp.route('/translate2', methods=["GET", "POST"])
def translate():
    if request.form:
        user_input_x = request.form.get("x_trans1")
        user_input_y = request.form.get("y_trans1")

        return_list = create_coord_list()
        return_list = translateBy(return_list, user_input_x, user_input_y, '')
        finalString = create_string(return_list)
        listToPass = str(return_list)

        return render_template("colin/college_board_polygon.html", active_page='colin', stringUse = finalString, listToPass = listToPass, numbList=return_list)

@colin_bp.route('/reset', methods=["GET", "POST"])
def reset():
    if request.form:
        return_list = create_coord_list()
        return_list = translateBy([], 0, 0, 'reset')
        finalString = create_string(return_list)
        listToPass = str(return_list)

        return render_template("colin/college_board_polygon.html", active_page='colin', stringUse = finalString, listToPass = listToPass, numbList=return_list)

@colin_bp.route('/network')
def network():
    return render_template('colin/network_map.html', active_page='colin')

@colin_bp.route('/solar')
def solar():
    return render_template('colin/planets.html', active_page='colin')

@colin_bp.route('/clone')
def clone():
    return render_template('colin/testingClone.html', active_page='colin')