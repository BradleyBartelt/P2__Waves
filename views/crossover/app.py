from flask import Blueprint, render_template, request
import requests, json
import pprint


crossover_bp = Blueprint('crossover_bp', __name__,
                          template_folder='templates',
                          static_folder='static',
                         static_url_path='assets')

@crossover_bp.route('/')
def index():
    # TODO: need to change out the url for the url on Mr.M's hardware
    #urlBase = "http://localhost:5005/"
    urlBase = "http://hawkers.nighthawkcodingsociety.com"
    url = str(urlBase) + "/apipull/tweets"
    userUrl = str(urlBase) + "/apipull/users"

    print(url)
    print(userUrl)

    response = requests.request("GET", url)
    dictionary = response.text
    textFromJSON = json.loads(dictionary)

    responseUser = requests.request("GET", userUrl)
    dictionaryUser = responseUser.text
    textFromJSONUser = json.loads(dictionaryUser)

    print("textFromJSON: " + str(textFromJSON))
    print(textFromJSONUser[0])

    frontEndList = []
    x = 0
    for post in textFromJSON:
        print(post)

        userIndex = post['user']
        print("index: "+str(int(userIndex)-1))
        user = textFromJSONUser[int(userIndex)-1]
        username = user['name']
        print(username)

        frontEndDict = {
            "username": username,
            "contents": post["tweetContent"]
        }

        frontEndList.append(frontEndDict)


    return render_template('crossover/pulling.html', response=textFromJSON, list=frontEndList)
