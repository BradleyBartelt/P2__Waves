# P2__Waves Piece of the Pie
Tri 3 project for P2__Waves

## [Project Plan](https://docs.google.com/document/d/1vByAzVE8BIA5xQ6L1B1xQvrMjikYDGONuw1jXJDoZHk/edit?usp=sharing)
Runtime link: http://www.pieceofthepi.cf/
### Idea
Our idea is to create a sort of Pizza revolved site, where you can order pizza, leave reviews, see deals, and more. We are going to take inspiration from the layout of other sites like dominos. In order to add a unique spin on it, we would like to impliment a feature where people can post pictures of the food they order and leave a reveiw, and other users can see the food and reviews, sort of like social media, but  for pizza.
#### Inspiration
- [Yelp](https://www.yelp.com/search?cflt=pizza&find_loc=San+Diego%2C+CA)
- [Dominos](https://pizza.dominos.com/california/san-diego/3485-del-mar-heights-rd/)
- [Pizza Hut](https://www.pizzahut.com/)
- [Reddit](https://www.reddit.com/)

#### Technicals/refrences
- [for subdomains](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [connecting Node.js with flask](https://medium.com/javarevisited/connecting-flask-with-node-js-7b9d823ca923) (for the direct messaging platform)

#### Contributors
<!-- the table of all of the members with the github username linked -->
|Name|	Github   | 
|--|--|
| Bradley Bartelt  |  [BradleyBartelt](https://github.com/BradleyBartelt) |
| Diego Krenz | [Diegokrenz](https://github.com/Diegokrenz) |
| Colin Szeto  |  [colin-szeto](https://github.com/colin-szeto) |
| Andrew Zhang | [Ketherbug](https://github.com/Ketherbug) |

#### [Scrum board](https://github.com/BradleyBartelt/P2__Waves/projects/1) 
#### [Deployed](http://www.pieceofthepi.cf/)

## Change log
### 2 week left of school

### week 9 
- Colin 
    - [using mongo db with sockets](https://developer.mongodb.com/how-to/real-time-chat-phaser-game-mongodb-socketio/)
    - planing for chatting rooms  (mongo db and socketio conflict)
        - will deploy chat room in separate website that will be linked on the nav bar, on click will log you into the chat room website
        - utilizing api to share information between the websites, signing up on the main site will be utilized onto the chat app
    - [how to only allow access through redirecting through spceific website](https://stackoverflow.com/questions/31131636/flask-to-only-allow-access-to-page-internally)

### week 8 (progress for week of 5/24/21)
- week of the College Board Exam
- outlined the 4 interactions of the project 
    - API formatting - reviews on the pizza
    - Chatting between users - () [video series](https://www.youtube.com/watch?v=uJC8A_7VZOA&list=PLyb_C2HpOQSBUEDI7tx_W4hAz699B6D7p) | [python socket](https://www.youtube.com/watch?v=3QiPPX-KeSc)
    - Uploading Posts - (POST)
    - Navigating External API - [see dominos](https://github.com/ggrammar/pizzapi)
    
- Colin 
    - going to be pivoting from sqlite (local database), and pivoting to a cloud database using MongoDB. 
    This is going to resolve the problems with merging local versions of databases. 
      - using MongoDB Atlas 
      - [documentation for MongoDB Atlas](https://docs.atlas.mongodb.com/)
      - [documentation MongoDB w3 schools](https://www.w3schools.com/python/python_mongodb_getstarted.asp)
    - great tool to learn about git [article](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-reset.html) | [discussion](https://intellij-support.jetbrains.com/hc/en-us/community/posts/206884545-How-to-undo-a-commit-in-a-local-branch-git)

    

### week 7 (progress for week of 5/17/21)
- College board submission week
- Colin
    - [ticket College Board](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-61268306)
    - [ticket PBL](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-60810362)
### week 6 (progress for week of 5/10/21)
- Colin
    - [Ticket #1:](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-60810362)
        - [runtime link](http://pieceofthepi.cf/colin/api_pull),
        - [Frontend code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/colin/templates/colin/api_pull.html),
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/4d359237a2c4984778ea24b2229f5a5906f315dc/views/colin/templates/colin/api_pull.html#L76-L95) implementation of js to display number of stars based off integer of rating of review
        - Backend Code
          - [code](https://github.com/BradleyBartelt/P2__Waves/blob/0579ad9946b8587c1b2031743213645070846e61/model/module.py#L172-L196) worked on getting the getters up for publishing database information in an API
                  - using workaround to map information from database into a list of json (each item within the list is a JSON which represents each row of data)
              - this is as the database file init is not in the app.py (highest level route management)

          - [code](https://github.com/BradleyBartelt/P2__Waves/blob/0579ad9946b8587c1b2031743213645070846e61/app.py#L35-L36) location where api routes are within the code
          - [Code backend to choose random review from database](https://github.com/BradleyBartelt/P2__Waves/blob/7c4cc355f728e8c73c92581888e6b84f8e5bd7db/views/colin/app.py#L217-L234)
          - [first counts number of entries in database](https://github.com/BradleyBartelt/P2__Waves/blob/7c4cc355f728e8c73c92581888e6b84f8e5bd7db/views/colin/app.py#L219-L224)
          - [choose entry to display based off random selection of all entries in database](https://github.com/BradleyBartelt/P2__Waves/blob/7c4cc355f728e8c73c92581888e6b84f8e5bd7db/views/colin/app.py#L226-L234) 
        
    - [Ticket #2](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-60811255):
        - Objective, to create listeners dynamically based off presets (precursor to linking the network map with the database)
        - [Runtime link](http://pieceofthepi.cf/colin/network) see buttons on right side of screen
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/4152cf5a228c38db290af4b8748b9f6531188ffa/views/colin/templates/colin/network/network_map.html#L39-L69) Old way in storing presets
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/4152cf5a228c38db290af4b8748b9f6531188ffa/views/colin/templates/colin/network/network_map.html#L71-L82) using jinja for loops to iterate through data
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/colin/algo/network_store.py) preset info stored in external python document
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/4152cf5a228c38db290af4b8748b9f6531188ffa/views/colin/templates/colin/network/network_map.html#L810-L822) Failed attempt in creating listeners dynamically, will explore using [.this](https://learn.jquery.com/events/event-delegation/) to read the value of selected item and use the children to find the id of corresponding tags storing values

### week 5 (progress for week of 5/3/21)
- Colin 
    - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/colin/templates/colin/network/network_map.html) [runtime link](http://pieceofthepi.cf/colin/network) worked on networking diagram maker 
        - lessons learned: use the canvas for drawing lines 
        - simple is usually better
    - worked on connecting database with API [forked code](https://github.com/colin-szeto/flask_api_sql)
    - Prototypes made
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/colin/templates/colin/rabbit_racer.html) rabbit racer from Khan academy
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/colin/templates/colin/planets.html) planets from khan academy (learning about appending children to parents)
        - [code](https://replit.com/@colinszeto/rotating#index.html) testing to see how div would interact with transform: rotate(180deg)
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/colin/templates/colin/network/test_drag.html) testing if making connections by rotating div would work
            - used points to document where the mousedown and mouse up occured
    
### week 4 (progress for week of 4/26/21)
- Colin 
    - worked on the admin page
        - worked on connecting up the database information to be shown in the front end
    - worked on college board submission redrawing polygon based off of user input
    
### week 3.5 spring break (4/19/21)
### week 2 (3/29/21) - 3 (4/5/21) Python Mini Labs

### Colin
- [link to runtime](http://www.pieceofthepi.cf/colin/) (this is the landing page, please ignore fibonacci as it was a reference for myself)
- [link to runtime](http://www.pieceofthepi.cf/colin/conversion) (this is the real mini lab, all decriptions and instructions are on the page)
    - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/colin/algo/conversion.py) (backend)
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L8) defining a class
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L35-L38) initializing objects from a class
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L42-L146) defining objects
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L42-L47) Decimal to Hex Converter, really for error handeling if ther was no input (will be explianed later on
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L49-L128) Hex to binary converter, attempted to user b != '' to provided different conversions based on what parameter was passed in, if b was passed in the object would convert b to binary, if b was not passed the object convert the user input into the class to binary (I have since learned that objects cannot refrence one another in a class) so currently b is force to '' to deflut to converting the parameter passed into the class to binary
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L130-L146) here is the object which formats the code ready to be itterated through (see below for more details)
    - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L149-L163) getters
    - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/colin/templates/colin/conversion.html) (front end)
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/templates/colin/conversion.html#L72-L78) using objects to format getters, I am able to itterate through the data with jinja loops
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L130-L146) here is the object which formats the code ready to be used
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/algo/conversion.py#L161-L163) here is the getter for the dictonary formatting of the code
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/app.py#L42) here is the location of the route where the getter is redefined "ist_conversion=conversion._list" so that it can be used in the jinja for loop
- WOW
    - my wow is definitely how I use two forms to pull objects from the same class
    - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/templates/colin/conversion.html#L35-L57) in the front end I have two diffrent forms that are shown based on selection with [javascript](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/templates/colin/conversion.html#L114-L144) (using the lessons that Mr. Matt presnted about this week) or using data passed in from the route [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/templates/colin/conversion.html#L151-L158)
    - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/app.py#L28) in the back end of routes, I see iff the single input was filled
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/app.py#L31-L42) if the single field was not filled, we can assume that the user filled out the multi filed form and restrict the values that are taken from the form and inputted into the class for our getters
        - [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/app.py#L44-L46) if so then (single field was filled), we can pull from the single field and pass it into the class for our desired values
        - notice when different routes are called for different inputs we specify which table we want to see
            - type_js=json.dumps('multi') [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/app.py#L42)
            - type_js=json.dumps('single') [code](https://github.com/BradleyBartelt/P2__Waves/blob/d11cb14158917dac2b552e9a4a590098643e3731/views/colin/app.py#L46)


### Andrew
- Link to project in runtime: http://www.pieceofthepi.cf/andrew/
- link to Html code: https://github.com/BradleyBartelt/P2__Waves/blob/main/views/andrew/templates/mini_lab.html
- link to Python code: https://github.com/BradleyBartelt/P2__Waves/blob/main/views/andrew/minilab.py
- Other Python file: https://github.com/BradleyBartelt/P2__Waves/blob/main/views/andrew/app.py
### Bradley
- Link to project in runtime: http://www.pieceofthepi.cf/bradley/
- link to Html code: https://github.com/BradleyBartelt/P2__Waves/blob/main/views/Bradley/templates/minilabB.html
- link to Python code: https://github.com/BradleyBartelt/P2__Waves/blob/main/views/Bradley/binary.py
- Other Python file: https://github.com/BradleyBartelt/P2__Waves/blob/main/views/Bradley/app.py
### Diego
    
### week 1 (Tickets for 3/26/21)

 - Homepage Template and Navbar (Bradley) [ticket](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-57623685)
   - This week I found an HTML template for our homepage, and created the navbar for our website. I am currently linking our HTML templates to the navbar, but we only have 2 at the moment, so some of the links will not be active.
   - (all the files in this link) Link to front end [code](https://github.com/BradleyBartelt/P2__Waves/tree/main/templates)
   - Link to python [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/app.py)
   - (really just the app routes in there)
   - link to runtime main page with navbar http://www.pieceofthepi.cf/
     
- User Profile Homepage and deployment (Colin)
    - [ticket](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-57444830)
        - worked on the user profile page this week
        - Front in
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/profile/templates/profile/user_profile.html) 
            - [deployed runtime link](http://www.pieceofthepi.cf/profile/userprofile)
        - Backend
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L14-L150) heavily used 'background-color' to differentiate between the divs to focus on the layout and spacing of the code
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/profile/models/temp_info.py) temporary backend, will replace with reading information from the database
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L229-L271) **WOW** using [listeners](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L231-L234) to communicate which button was selected and to avoid inline javascript, using [procedures](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L253-L267) by taking in [parameters](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L238) to determine which [div](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L199-L225) to show and which div to hide
        - Mini Lab location 
            - [runtime](http://www.pieceofthepi.cf/colin/)
            - [blueprint](https://github.com/BradleyBartelt/P2__Waves/tree/main/views/colin)
-  User Database and login (Andrew)
    - [ticket](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-57787718)
-  Blueprint setup (Diego)
    - [ticket](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-57650333])

## Pull code from Github and update packages
#### In console/terminal (every update: pull code and check package dependencies)...

pi@raspberrypi:~ $  ``` sudo apt update; sudo apt upgrade```

pi@raspberrypi:~ $  ``` cd ~/P2__Waves```

pi@raspberrypi:~/P2__Waves $ ```  git pull```

pi@raspberrypi:~/P2__Waves $ ```  source wave/bin/activate```

#### In console/terminal with virtualenv activitate (every time: check and update packages)...

(wave) pi@raspberrypi:~/P2__Waves $ ```  sudo pip install -r requirements.txt```

#### In console/terminal (every time AFTER initial setup: restart gunicorn)...

pi@raspberrypi:~ $ ```sudo systemctl restart  wave.service```

### Credit
- [Favicon Used](https://www.deviantart.com/chinyiun/art/Pixel-art-pizza-852260462)
