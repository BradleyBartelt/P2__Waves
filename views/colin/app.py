from flask import Blueprint, render_template, request
# from views.profile.models import temp_info
from views.colin.algo.fibonacci import Fibonacci
from views.colin.algo.conversion import Conversion
from views.colin.algo.bubble_sort import BubbleSort
from views.colin.algo.bubble_sort2 import BubbleSortString
import json, random, requests
from views.colin.algo.network_store import list_store
from model.module import RatingFood, CreateReview, review_info, db, SQLAlchemy, api, func
from datetime import datetime

# for connecting mongo db (form front end)
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

# for pushing to mongo db
from model.chat_db import *

colin_bp = Blueprint('colin_bp', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=0, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=0, max=80)])

# default landing page that use arrives when clicking the colin button in nav bar
@colin_bp.route('/')
def index():
    return render_template('colin/.mini_lab_landing.html', active_page='colin')

# testing a template found on the w3 school site
@colin_bp.route('/template')
def school():
    return render_template('colin/w3school.html', active_page='colin')

# testing out the program code Mr. M provided that demonstrated using Classes
@colin_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("colin/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))), active_page='colin')
    return render_template("colin/fibonacci.html", fibonacci=Fibonacci(2), active_page='colin')

# code for bubble sort (mini lab) how to sort inputs based on value or length of word
@colin_bp.route('/bubblesort', methods=["GET", "POST"])
def bubblesort():
    if request.form:
        # list that contains info to display on frontend
        all_list = []

        # getting the number of inputs added from hidden input field
        newbox_counter = request.form.get('newbox_counter')
        newbox_counter_string = request.form.get('newbox_counter_string')
        print('number of boxes added' +str(newbox_counter))
        print('number of boxes added string' +str(newbox_counter_string))

        # getting what type of vlaue are we sorting integer or string
        input_type = request.form.get('input_type')
        print(input_type)

        # if the selection was integer
        if input_type == 'integer':
            b = 1 # to ensure first number is 1 (used in identifying id to sample from)
            numberToItterate = 5 + int(newbox_counter)
            # iterating through all of the form text fields input
            for i in range(numberToItterate):
                # getting the field to sample from
                string_used = 'user_input' + str(b)
                user_input = request.form.get(string_used)
                print(user_input)

                # adding that field value into the all list
                all_list.append(int(user_input))
                b = b + 1

            print(all_list)
            bubble = BubbleSort(all_list)
        else:
            # if the number was string
            b = 1 # to ensure first number is 1 (used in identifying id to sample from)
            numberToItterate = 5 + int(newbox_counter_string)
            # iterating through all of the form text fields input
            for i in range(numberToItterate):
                # getting field to sample from
                string_used = 'user_input_string' + str(b)
                user_input = request.form[string_used]
                print('value of ' + str(string_used) +': '+ str(user_input))

                # adding that field value into all list
                all_list.append(user_input)
                b = b + 1

            print(all_list)
            # taking all list (type list) and passing it as a parameter into a class
            bubble = BubbleSortString(all_list)

        # displaying the sorted list in the front end
        return render_template("colin/bubble_sort.html", active_page='colin', output_list = bubble.OuputList)

    # default page user sees
    return render_template("colin/bubble_sort.html", active_page='colin')

# end of bubble_sort

# to take in user input and display the conversion
@colin_bp.route('/conversion', methods=["GET", "POST"])
def conversion():

    # when there is a user input within the code
    if request.form:
        #  getting the input of a single field
        user_input = request.form.get('user_input0')
        print(str(user_input))

        if user_input == None:
            # if the user input (single field) was not filled. This implies that the multi field butto was selected
            all_list = []
            b = 1 # to ensure first number is 1

            # itterating through the number of input fields and appending values inot a list
            for i in range(5):
                string_used = 'user_input' + str(b)
                user_input = request.form.get(string_used)
                all_list.append(int(user_input))
                b = b + 1
            print(all_list)
            # passing in list as second parameter (placement denotes that this is a list)
            conversion = Conversion('', all_list)
            return render_template("colin/conversion.html", user_input=user_input, conversion=conversion,
                                   list_conversion=conversion._list ,active_page='colin', type='multi', type_js=json.dumps('multi'))
        else:
            # if the user input is not zero (it was filled)
            # notice value passed in as first parameter (placement denotes that this is only a single vlaue )
            conversion = Conversion(user_input, '')
            return render_template("colin/conversion.html", user_input=user_input, conversion=conversion, active_page='colin',
                                   type='single', type_js=json.dumps('single'))

    # default configuration,
    conversion = Conversion(0, [1,2,3,4,5,6,7,8])
    return render_template("colin/conversion.html", conversion=conversion, list_conversion=conversion._list ,active_page='colin')

""" College Board Code"""


# reading all 6 inputs corresponding to each coordinate of the polygon and formatting
# it into a list of (x1,y1,x2,y2,x3,y3)
def create_coord_list():
    all_list = []
    b = 1  # to ensure first number is 1, used in specifying inputs to sample from
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


# to convert the initial coordinates of the polygon (stores in a list) into a string
# (format to update the coordinates of the polygon)
def create_string(return_list):
    # initializing the string
    coord_string = ''
    # iterating through the length of the list
    for i in range(len(return_list)):
        # to skip placing a comma in front of the first number (ensures
        # ",200,10,250,190,160,210" does not happen)
        if i > 0:
            coord_string = coord_string + "," + str(return_list[i])
        else:
            # concatenate "number," to the string
            coord_string = coord_string + str(return_list[i])
    return coord_string


# initial coordinates of the polygon
inital_coords = [200, 10, 250, 190, 160, 210]


# running the procedure to convert the list into a string (readable format to update the
# coordinates of the polygon)
inital_string = create_string(inital_coords)


# procedure/algorithm that is highlighted in the wr portion (translates coordinates based
# off uniform translation)
def translateBy(res, valuex, valuey, state):
    if state == 'reset':
        res = inital_coords
    else:
        for i in range(len(res)):
            if i % 2 == 0:
                # if the value is in 0,2,4,6,8 place add the x displacement
                x_coord = int(res[i])
                x_displacement = int(valuex)
                res[i] = x_coord + x_displacement
            else:
                # if the value is in 1,3,5,7,9 place add the y displacement
                y_coord = int(res[i])
                y_displacement = int(valuey)
                res[i] = y_coord + y_displacement
    return res


# procedure to manipulate individual coordinates or manipulate each coordinate in their
# unique translation (not all coordinates have to have a uniform translation of +20 x
# displacement)
@colin_bp.route('/polygon', methods=["GET", "POST"])
def polygon():
    if request.form:
        return_list = create_coord_list()
        finalString = create_string(return_list)
        listToPass = str(return_list)
        print("list to pass: " + str(listToPass))
        return render_template("college_board_polygon.html", stringUse=finalString, listToPass=listToPass,numbList=return_list)

    # on first navigation display the default coordinates
    return render_template("college_board_polygon.html", stringUse=inital_string, numbList=inital_coords)


# if the translate button is selected
@colin_bp.route('/translate', methods=["GET", "POST"])
def translate():
    if request.form:
        # get the user input for displacement of all coordinates
        user_input_x = request.form.get("x_trans1")
        user_input_y = request.form.get("y_trans1")

        # get the current position of the polygon
        return_list = create_coord_list()

        # translate all current coordinates of the polygon by the displacement
        # specified earlier
        return_list = translateBy(return_list, user_input_x, user_input_y, '')

        # format information in string data type used to redraw the polygon)
        finalString = create_string(return_list)
        listToPass = str(return_list)

        return render_template("college_board_polygon.html", stringUse=finalString, listToPass=listToPass, numbList=return_list)


# to reset the polygon to the original position
@colin_bp.route('/reset', methods=["GET", "POST"])
def reset():
    if request.form:
        # passing in 4 parameters, string 'reset' will ensure that the polygon coordinates
        # are set back to their original values
        return_list = translateBy([], 0, 0, 'reset')

        # format information in string data type used to redraw the polygon)
        finalString = create_string(return_list)
        listToPass = str(return_list)

        return render_template("college_board_polygon.html", stringUse=finalString, listToPass=listToPass, numbList=return_list)


"""End College Board Code"""
@colin_bp.route('/network')
def network():
    return render_template('colin/network/network_map.html', active_page='colin', parent_list=list_store)

@colin_bp.route('/solar')
def solar():
    return render_template('colin/planets.html', active_page='colin')

@colin_bp.route('/clone')
def clone():
    return render_template('colin/testingClone.html', active_page='colin')

@colin_bp.route('/rabbit_racer')
def rabbit_racer():
    return render_template('colin/rabbit_racer.html', active_page='colin')

@colin_bp.route('/network_div')
def network_div():
    return render_template('colin/network/network_map_div.html', active_page='colin')

@colin_bp.route('/test_drag')
def test_drag():
    return render_template('colin/network/test_drag.html', active_page='colin')

@colin_bp.route('/api_pull')
def api_pull():
    # getting the qunaity of row entries to use for the random selection
    urlList = "http://site.pieceofthepi.cf/AllFood"
    response_list = requests.request("GET", urlList)
    all_list = json.loads(response_list.text)

    # getting a random field from the entire database len(all_list) corresponds to number of rows in database
    url = "http://site.pieceofthepi.cf/Food/" + str(random.randint(1, len(all_list)))
    response = requests.request("GET", url)

    # current the request
    dictionary = response.text
    y = json.loads(dictionary)
    return render_template('colin/api_pull.html', active_page='colin', data = y)

# backend post (writing directly to the database) cannot be inserted into crossover's backend
@colin_bp.route('/api_form', methods=["GET", "POST"])
def api_form():
    if request.form:
        # getting information from the backend FORM
        restaurant = request.form.get('restaurant')
        name = request.form.get('name')
        star_count = request.form.get("star_count")
        message_input = request.form.get("message")

        message = str(restaurant) + " "+ str(name) + " " + str(star_count) + " "+ str(message_input)
        default_message = "Restaurant Name Your name here 0 Leave Comments Here"

        # from the backend ensuring that the correct number is assigned based off max count in database
        userid = int(db.session.query(func.max(RatingFood.id)).scalar())+1
        print(userid)

        # getting the current time
        now = datetime.now()

        # filling in the data to populate the database
        review = RatingFood(
            id=userid,
            restaurant=restaurant,
            name=name,
            user="peasant",
            time=now,
            stars=int(star_count),
            description=str(message_input)
        )
        print(review.json())

        # committing information into the database
        db.session.add(review)
        db.session.commit()

        return render_template('colin/api_form.html', active_page='colin')

    return render_template('colin/api_form.html', active_page='colin')

@colin_bp.route('/api_form_POST', methods=["GET", "POST"])
def api_form_POST():
    if request.method == 'POST':
        # getting the information from the form
        restaurant = request.form.get('restaurant')
        name = request.form.get('name')
        star_count = request.form.get("star_count")
        message_input = request.form.get("message")

        # formatting information into the URL use to access the API
        url_info = 'http://pieceofthepi.cf/createReview/' + str(restaurant) + "/" + str(name) + "/peasant/" +str(star_count) + '/'+str(message_input)
        print(url_info)

        # POST to the API
        requests.post(url_info)

        # render the default page
        return render_template('colin/api_form_POST.html', active_page='colin')

    return render_template('colin/api_form_POST.html', active_page='colin')

@colin_bp.route('/signupColin', methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        # printing the form information in the terminal
        # print(form.username.data)
        # print(form.email.data)
        # print(form.password.data)

        save_user(form.username.data, form.email.data, form.password.data)

        return '<h1>yay</h1>'

    return render_template("colin/sign_up.html", form=form)

@colin_bp.route('/searchTable')
def serachTable():
    return render_template("colin/searchTable.html")
