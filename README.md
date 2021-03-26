# P2__Waves Piece of the Pie
Tri 3 project for P2__Waves

<!-- the table of all of the members with the github username linked -->
|Name|	Github   | 
|--|--|
| Bradley Bartelt  |  [BradleyBartelt](https://github.com/BradleyBartelt) |
| Diegokrenz | [Diegokrenz](https://github.com/Diegokrenz) |
| Colin Szeto  |  [colin-szeto](https://github.com/colin-szeto) |
| Andrew Zhang | [Ketherbug](https://github.com/Ketherbug) |

####[scrum board](https://github.com/BradleyBartelt/P2__Waves/projects/1) 
####[deployed](http://76.167.66.16:5000/)

## Change log

### week 1 (Tickets for 3/26/21)

 - Homepage Template and Navbar (Bradley) [ticket](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-57623685)
   - This week I found an HTML template for our homepage, and created the navbar for our website. I am currently linking our HTML templates to the navbar, but we only have 2 at the moment, so some of the links will not be active. 
     
- User Profile Homepage and deployment (Colin)
    - [ticket](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-57444830)
        - worked on the user profile page this week
        - Front in
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/profile/templates/profile/user_profile.html) 
            - [deployed runtime link](http://76.167.66.16:5000/profile/userprofile)
        - Backend
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L14-L150) heavily used 'background-color' to differentiate between the divs to focus on the layout and spacing of the code
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/main/views/profile/models/temp_info.py) temporary backend, will replace with reading information from the database
            - [code](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L229-L271) **WOW** using [listeners](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L231-L234) to communicate which button was selected and to avoid inline javascript, using [procedures](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L253-L267) by taking in [parameters](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L238) to determine which [div](https://github.com/BradleyBartelt/P2__Waves/blob/4dec3a55ad83f5b10a0ab74c74ea226474b2ceff/views/profile/templates/profile/user_profile.html#L199-L225) to show and which div to hide
-  User Database and login (Andrew)
    - [ticket](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-57787718)
-  Blueprint setup (Diego)
    - [ticket](https://github.com/BradleyBartelt/P2__Waves/projects/1#card-57650333])
## [Project Plan](https://docs.google.com/document/d/1vByAzVE8BIA5xQ6L1B1xQvrMjikYDGONuw1jXJDoZHk/edit?usp=sharing)
### Idea
Our idea is to create a sort of Pizza revolved site, where you can order pizza, leave reviews, see deals, and more. We are going to take inspiration from the layout of other sites like dominos. In order to add a unique spin on it, we would like to impliment a feature where people can post pictures of the food they order and leave a reveiw, and other users can see the food and reviews, sort of like social media, but  for pizza.

#### Inspiration
- [Yelp](https://www.yelp.com/search?cflt=pizza&find_loc=San+Diego%2C+CA)
- [Dominos](https://pizza.dominos.com/california/san-diego/3485-del-mar-heights-rd/)
- [Pizza Hut](https://www.pizzahut.com/)
- [Reddit](https://www.reddit.com/)

#### Technicals
[for subdomains](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
