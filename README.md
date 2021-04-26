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

## Python Mini Labs
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
### week 5 (progress for week of 4/26/21)
- Colin 
    - worked on the admin page
        - worked on connecting up the database information to be shown in the front end
    
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

### Credit
- [Favicon Used](https://www.deviantart.com/chinyiun/art/Pixel-art-pizza-852260462)