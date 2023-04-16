![TWS Screens](media/all-devices-black.png)

# TWS -Together we Shred

## Design Brief
The site was created to support my nephews (will refer to as TWS Owner)  new business - TWS (Together we Shred). It is a lifestyle clothing brand aimed at the motocross and mountain biking community. The range of clothing is designed to be comfortable, practicable, of a high quality but also have an image that represents the customers in the motocross and mountain biking community, and make people want to but the brand based on its image.  He is very much trying to create a brand, the shared love of getting out and riding together and sharing those experiences.The company is active on Instagram and Facebook however lacks an ecommerce presence. 

## Early Challenge Identified as part of brief
Ensuring that the ecommerce site reflects the brand, shows that I have developed this myself, and can demonstrate my skills and not just follow the boutique_ado site, and make small amendments.  I did question if I should do a different site but it was important to me to try and deliver an ecommerce site that could with some minor work be used in the real world, and was a real use case. 

# Strategy Plane - UX
## Project Goals 
Together We Shred is a full stack e-commerce website built using Django, Python, HTML, CSS and JavaScript. The website uses Stripe as the payment processor.
It was developed for my final assignment to showcase the skills I have learnt during the Code Institute Level 5 Diploma course.
The ecommerce site, had to meet, and represent the brand, be of high quality and have potential to be used to help improve TWS Owners business and increase ability to generate income. 

## Audience

* Guest - aimed at riders of Mountain bikes, Motocross riders, and the supporters in that area who are looking for a clothing brand.
* Registered USers -returning vistors to the site who regularly purchase and are interested in exclusive discounts
* Admin - admins being able to add, update prodcuts to shop with an easy interface.

## Why ?
The site was created to support my nephews new business - TWS (Together we Shred). I hoped it could help generate an income for him with, and with some further devleopment be a valuable part of his business.

# Scope Plane - UX
I have tried to plan the site, from a user perspective and administrative perspective. 
This will then lead me to design my Database Schema, allow me to identify priorities for the project from a TWS Owner , Administrator of site and customer perspective.

Priorities and requirements may change later on, to ensure I meet the criteria of the Assignment as well as TWS Owners  requirements. 

Importance 1 - 5 with    
1 being nice to have 
5 being essential

To enable me to develop a MVP, Focus of user stories was those with a priority of 4 and 5, I also added the User Story ID 11 even though a priority of 3, to satisfy the need for additional unique models as part of the course requirements.

| ID | Process          | As A/An  | I Need To Be Able To                              | So That I Can                                                                                       | Importance |
|----|------------------|----------|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|------------|
| 1  | Site             | Customer | Understand purpose of site quickly and clearly    | Decide if I am on the correct site and suits my needs                                               | 5          |
| 2  | Product          | Customer | Browse the site easily                            | Find products quickly and easily                                                                    | 5          |
| 3  | Product          | Customer | Filter Products                                   | Find products based on category i.e hoodies, hats.                                                  | 3          |
| 4  | Product detail   | Customer | View detailed information about specific products | So I can see more details about the product, and a larger more detailed image.                      | 5          |
| 5  | Purchase         | Customer | Add Items to shopping bag                         | Store these for purchase                                                                            | 5          |
| 6  | Purchase         | Customer | Increase and decrease quantities easily           | So that I can quickly purchase more of the same item, or reduce the number of items                 | 5          |
| 7  | Purchase         | Customer | See total of items in shopping bag                | Identify how much I am currently spending                                                           | 4          |
| 8  | Purchase         | Customer | Remove items from shopping bag                    | In case I decide I no longer want these items                                                       | 4          |
| 9  | Checkout/Payment | Customer | Items purchasing, and total amount to pay         | Checkout quickly and easily                                                                         | 5          |
| 10 | Checkout/Payment | Customer | Pay for items securely                            | Have confidence that my order, and money is processed safely.                                       | 5          |
| 11 | Checkout/Payment | Customer | Add a voucher code                                | So that I can apply a discount to my order                                                          | 3          |
| 12 | Checkout/Payment | Customer | Receive payment and order on-screen feedback      | Confident that payment has been processed and order is being processed                              | 4          |
| 13 | Checkout/Payment | Customer | Receive confirmation email                        | Confident of items ordered, amount paid and have contact details of the company in case of queries. | 4          |
| 14 | User Profile     | Customer | Register for an Account                           | So I can store my address details                                                                   | 5          |
| 15 | User Profile     | Customer | Login / Logout                                    | Keep my personal information secure                                                                 | 5          |
| 16 | User Profile     | Customer | View My Profile                                   | View details I have stored with the site                                                            | 5          |
| 17 | User Profile     | Customer | Edit My Profile                                   | I can update my address, for example                                                                | 5          |
| 18 | User Profile     | Customer | Login with Social media account                   | So I can be quickly and easily registered with the site                                             | 2          |
| 19 | Product Admin    | Admin    | Show/Highlight Popular Items                      | To tempt people into buying these items                                                             | 2          |
| 20 | Product Admin    | Admin    | Add Products                                      | Add new products to the website quickly and easily for customers to view                            | 5          |
| 21 | Product Admin    | Admin    | Edit Products                                     | Edit details of existing products, for example if other colours become available, or price changes. | 5          |
| 22 | Product Admin    | Admin    | Delete Products                                   | Remove products that no longer sell                                                                 | 5          |
| 23 | Marketing        | Admin    | Send promotional emails                           | To encourage customers to purchase and shop with us                                                 | 3          |
| 24 | Marketing        | Admin    | Understand shopping trends                        | So the brand can move with the times and produce more of the products customers want                | 3          |

# Structure Plane - UX
Below is a structure of the site I decided to use a swimlane approach, helped me identify areas of site that needed to be built first, and how the different functions for different users build on each other.

![swimlane guest](media/swimlane_guest.PNG)
![swimlane registers](media/swimlane_registered.PNG)
![swimlane admin](media/swimlane_admin.PNG)

## DB schema
Below is the intial mapping out of the Database structure, based on the requirements identified. This was done to help me visualise how they interlink and primarark and foreign keys needed. It would also give me an opportunity to review and make future improvements. Some fields were added and not used, this was becuase my focus was on prpdcuing a Minimal Viable prpdcut to satisfy the course requirements, rather than a perfect solution at the 1st attempt. I felt including the fields would help me make these improvements quicker later on. 

![db schema](media/dbschema.PNG)


# Skeleton Plane - UX
## Handrawn
I roughly drew out the layout, and what i felt the site would look like, some images below.

![home handdrawn](media/handdrawn_home.PNG)
![checkout handrawn](media/checkouthandrdrawn.PNG)

## wireframes
I created some inital wireframes for the main areas of the site, and would use these as a basis for the rest of my site.

![home wireframe](media/home_wireframe.PNG)
![shop wireframe](media/shop_wireframe.PNG)
![productdetail wireframe](media/productdetail_wireframe.PNG)


# Surface Plane - UX

## Design Inspiration
TWS Owner provided several websites that they like the look off, however the website www.24mx.co.uk was a site that the layout was most simliar to what they had visualised. It was clean and fresh.The TWS logo was already a black and white image, which represented the brand perfectly, and was main basis for the colour scheme,with splashes of colour to focus user for any Call to actions.
![24mx screenshot](media/24mxscreenshot.PNG)

## Colour scheme
TWS logo was black and white, and this was very much the brand, and fitted the target audience.

![colour pallete](media/maincolorpallete.PNG)

## Typography
The font used was Montserrat, it is a very clean font, and with the use of weights was able to emphasis areas on the website.

# Features

## Header
The header contains the company logo for tws and this is the most important aspect, so visitors to the site see th ebrand straight away.
I have included the shopping cart and when images are added or removed the item total increases or decreases

![header](media/header.PNG)

## Navigation
The navigation contains links ot the main areas of the site, the login, signup buttons adjust dependendant on if you are a guest
### Guest user
![guest nav](media/navbar.PNG)

### registered user
Have the ability to create a profile and update their address details, to improve the checkout process. We will also register there detials and use this to send out unique discount codes, special offers.
![registered nav](media/navbar_registered.PNG)
## admin user 
Admin users are able to manage aspects of the website, with CRUD fucntionality for the products database.
![admin nav](media/navbar_admin.PNG)




# Testing 
## lightohose
## css, html, JS, Python test

## Testing user stories  

# technologies used

## issues

# deployment

# future devlelopments

# credits and thanks 
My Nephew(Rhys Railey)
for allowing me to prpdcut this for his brand

Code Institute
Basis of project was from Task project as part of my CI course

Spence Bariball (Mentor)
Helping to keep me motivated, and being supportive throughout.

Tutor Assistance




To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
