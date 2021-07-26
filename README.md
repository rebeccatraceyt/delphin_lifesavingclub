<h1 align="center">
     <a href="" target="_blank"><img src="" alt="Delphin Logo"></a>
</h1>

<div align="center">
<p>The <strong>Delphin Lifesaving Club</strong> e-shop was designed, built and deployed by Rebecca Tracey-Timoney as the fourth and final Milestone Project to be completed for the duel Software Development Diploma from The Code Institute and UCD. The purpose of this online shop is to provide a virtual shopping environment for club members (future and current) to browse and purchase Delphin products, including classes and club apparel. The website provides a smooth and uncomplicated online shopping experience for users, with its simplistic and intuitive design.</p>

[View the live project here]( "Link to Delphin page")
<hr>
</div>

### Table of contents
1. [UX](#UX)
     1. [Project Goals](#Project-Goals)
     2. [User Stories](#User-Stories)
     3. [Development Planes](#Development-Planes)
2. [Information Architecture](#Information-Architecture)
3. [Features](#Features)
     1. [Design Features](#Design-Features) 
     2. [Existing Features](#Existing-Features)
     3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Languages](#Languages)
     2. [Tools](#Tools)
     3. [Libraries](#Libraries)
     4. [Database Management](#Database-Management)
6. [Testing](#Testing) ☞ **[Testing.md](TESTING.md)**
7. [Deployment](#Deployment)
     1. [1. Database Creation](#1-Database-Creation)
     2. [2. Local Copy Creation](#2-Local-Copy-Creation)
     3. [3. Heroku App Creation](#3-Heroku-App-Creation)
8. [Credits](#Credits)
9. [Acknowledgements](#Acknowledgements)
10. [Technical Support](#Technical-Support)
***

![Delphin Responsiveness](static/images/readme-files/responsive.png)

***

## UX 
### Project Goals
#### User Goals
The User is looking to:
- Securely purchase available Club courses
- Securely purchase club apparel
- Contact the Delphin Team
- Learn about the club (for prospective members)
- Navigate through the online store with ease  
#### Developer / Site Owner Goals
The Developer is looking to:
- Provide and professional and trustworthy webshop, helping users to meet their goals.
- Reach a wider audience of prospective members through online intergration, making it easier to get involved.
- Provide a seamless process, allowing swimmers to pre-purchase lessons, prior to registration, avoiding unnecessary waiting times on location.
- Showcase the variety of lessons that Delphin provides.
- Showcase the Club's apparel collection
- Demonstrate their proficiency in a variety of software development skills, using newly learned languages and libraries as well as a document database system.
- Deploy a project they are proud of, and excited to have, on their portfolio.

### User Stories

**As a user, I want to:**

1. View all products, to purchase my desired items.
2. Filter through categories, to only see relevant products.
3. Use a search query, to find a specific product or product type.
4. Sort items by price, name or category to identify products of interest.
5. Add items to my shopping bag, to begin the order process.
6. Receive visual feedback that my item has been added to the bag, to confirm my selection.
7. Select a course on a specific day, to suit my needs.
8. Select clothing in a specific size, to suit my needs.
9. View contact information for the club, to communicate with team.
10. Connect with the club on one of their social apps, to communicate with the team.
11. Read the latest posts of the club newsletter, to keep up to date with current club news.

**As a new visitor, I want to:**

1. View the club's mission, to ascertain if the club is right fit.
2. Complete the registration process, to create an account.

**As a returning visitor, I want to:**

1. Easily log into my existing account, to unlock registered user features.
2. View my previous orders, to keep a record of my transaction.
3. Save default information, to save time for future orders.
4. Edit default information, to update any necessary fields. 
5. View shopping bag to get an overview of products I wish to order.
6. Remove products from my bag, to suit my needs.
7. Update a product's quantity, to suit my needs.
8. Proceed to a secure checkout, to make a purchase.
9. Have clear visual feedback of the order process, to understand all steps of the process.
10. Be able to edit my bag at all times, to allow change of mind.
11. Receive a summary of my order via email to confirm that my transaction has been process.

### Development Planes

In order to design and create the application, the developer distinguished the required functionality of the site and how it would answer the user stories, as described above, using the **Five Development Planes**:

<strong>1. <u>Strategy</u></strong>

Broken into three categories, the website will focus on the following target audiences:
- **Roles:**
     - New Swimmers
     - Current Swimmers
     - Parents/Guardians of Swimmers

- **Demographic:**
     - Aged 16+ (to make a purchase)
     - Dublin (or neighbouring counties) resident
     - Active/Sporty
     - Swimming/Lifesaving Orientated

- **Psychographics:**
     - Personality & Attitudes:
          - Sporty
          - Outgoing
          - Team Orientated
     - Values:
          - Friendship
          - Community
          - Activeness
     - Lifestyles:
          - Sporty
          - Team Player
          - Outgoing

The website needs to enable the **user** to:
- Purchase a course
- Purchase Club Apparel
- Find out more about the club:
    - Club Mission
    - Club Origins/History
- Browse the Club newsletter
- Get in contact:
    - WhatsApp
    - Facebook
    - Email(mailto)
    - Phone
    - Contact Form

The website needs to enable the **client** to:
- Display all available course
- Provide a virtual shop for Club Apparel
- Provide club information:
    - Club Mission
    - Club Origins/History
- Provide a point of contact:
    - WhatsApp
    - Facebook
    - Email(mailto)
    - Phone
    - Contact Form

With these goals in mind, a strategy table was created to determine the trade-off between importance and viability with the following results:

**Opportunity Matrix for User Management:**
[Strategy Table for User Management]( "User Management Strategy Table")

**Opportunity Matrix for Transaction Management:**
[Strategy Table for Transaction Management]( "Transaction Management Strategy Table")


<strong>2. <u>Scope</u></strong>

A scope was defined to identify what needed to be done in order to align features with the strategy previously defined. This was broken into two categories:
- **Content Requirements**
     - The user will be looking for:
        - Product Information:
            - Name
            - Description
            - Image
            - Size (where applicable)
            - Day (where applicable)
        - Contact Information:
            - WhatsApp
            - Facebook
            - Email(mailto)
            - Phone Number
            - Contact Form
        - Club Newsletter
        - Create/Login to Profile
            - Save default information
            - View Previous Orders
        - Thematic Imagery and Typography
            - Club logo and colours
            - Typography matching club aesthetic

- **Functionality Requirements**
     - The user will be able to:
        - Search Products
            - Courses:
                - By Age
            - Clothing / SwimShop
                - By Type
        - Make Transactions
        - Sign Up / Login to profile
            - Edit Profile information
            - Delete profile
            - View Previous orders
            - View shopping bag
        - Interact with shopping bag
            - Add to bag
            - Review bag contents
            - Update bag contents (increase quantity)
            - Remove from bag
        - Read the latest newsletter posts

<strong>3. <u>Structure</u></strong>

The website's navigation was organized in order to ensure that users could navigate through the site with ease and efficiency, with the following results: 

**Navigation Structure for User Management:**
![Navigation Structure for User Management]( "User Management Navigation Structure")

**Navigation Structure for Product Management:**
![Navigation Structure for Product Management]( "Product Navigation Structure")

**Navigation Structure for Transaction Management:**
![Navigation Structure for Transaction Management]( "Transaction Navigation Structure")

<strong>4. <u>Skeleton</u></strong>

Wireframe mockups were created in a [Figma Workspace](https://www.figma.com/file/Hx5A1pBFoMZs2BYT781Te6/Delphin "Link to Delphin Workspace") with providing a positive user experience in mind:


**Post Mock-Up Design Changes:** </br>
While the developer relied heavily on these Wireframes in order to maintain the desired design, there are several differences between the Mockups and the final product:


<strong>5. <u>Surface</u></strong>


- <strong>Colour Scheme</strong>

     - The chosen colour scheme was specifically selected to match the club colours. They are representitive of Lifesaving equipment used, such as flags and lifebuoys.

     - The red colour is specific to Lifeguarding and is used to highlight anything Lifeguarding related.

     - The Blus is an accent colour used in the club logo and beyond for colour contrast.


- <strong>Typography</strong>

     - The primary font chosen is [Lato](https://fonts.google.com/specimen/Lato "Link to Lato Google Fonts page"). A humanist sans-serif typeface, Lato is semi-rounded with a structured, but friendly warmth.

        ![Lato Typeface Example]( "Lato Typeface Example")

     - The Secondary font (accent font) chosen is [Londrina Solid](https://fonts.google.com/specimen/Londrina+Solid "Link to Londrina Solid Google Fonts page"). A newfolk typeface, with a rough, handwritten feel, for versatile screen display.

        ![Londrina Solid Typeface Example]( "Londrina Solid Typeface Example")

     - The secondary font is an updated version of the font used in the club's typography for logo and official letters. The font is paired well with the primary font, in order provide a minimally contrasting font combination serving as a practical and professional typeface with a hint of playfulness. This highlights the club's character for being professional, yet friendly, setting the tone for new and unfamiliar vistiors.

- <strong>Imagery</strong>

     - The imagery used was created by the developer using the application [Procreate](https://procreate.art/ "Link to Procreate") in order to create a consistency of the elements while maintaining the look and feel of the application.

     - The product imagery used digital renderings of the available orders, with a complete list of credits in a separate file, found [here]()

[Back to top ⇧](#table-of-contents)

## Information Architecture
### Database
- During development, a single-database was setup using [SQLite](https://www.sqlite.org/index.html "Link to SQLite site") as this is included and did not require any further installation to support.
- Upon deployment, [Heroku Postgres](https://www.heroku.com/postgres "Link to Heroku Postgres site") was used, as this is an add-on service provided by Heroku.

### Data Models


## Features

### Design Features

### Existing Features

**[Home Page]( "Link to Home page")**
| Feature      | Description  |
|--------------|--------------|
|     |  |


### Features to Implement in the future


[Back to top ⇧](#table-of-contents)

## Issues and Bugs 

[Back to top ⇧](#table-of-contents)

## Technologies Used
### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
- [Python](https://www.python.org/ "Link to Python Homepage")

### Tools
- [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/ "Link to download Visual Studio Code Insiders") 
     - VSCode was used as the preferred IDE.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control to commit to Git and push to Heroku.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project repository, after pushing.
- [Heroku](https://id.heroku.com/login "Link to Heroku login page")
     -  Heroku was used in order to deploy the website.
purposes.
- [Django](https://www.djangoproject.com/ "Link to Django Homepage")
     - Django was used as the web framework for the application.
- [Figma](https://www.figma.com/ "Link to Figma homepage")
     - Figma was used to create the wireframes during the design phase of the project.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used in order to validate the responsiveness of the design throughout the process, and to generate mockup imagery to be used.
- [Procreate](https://procreate.art/ "Link to ProCreate homepage")
     - Procreate was used to create and edit images as well as using the colour picker tool to ensure consistency throughout.
- [Imgbb](https://imgbb.com/ "Link to Imgbb site") 
     - ImgBB was used to externally host images used.
- [Transparent Textures](https://www.transparenttextures.com/ "Link to Transparent Texures site")
     - Transparent Textures was used to create the textured background heavily featured on the website.
- [Font Awesome](https://fontawesome.com/ "Link to Font Awesome site")
     - Font Awesome was used in conjunction with Iconify for icons used throughout the website.

### Libraries
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [jQuery](https://jquery.com/ "Link to jQuery page")
     - jQuery was used to simplify the JavaScript code used.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts was used to import the fonts **"Indie Flower"** and **"Work Sans"** into the style.css file. These fonts were used throughout the project.
- [jQuery Validation](https://jqueryvalidation.org/ "Link to jQuery Validation page")
     - jQuery Validation was used to simplify form validation for the **Contact Form**.
- [SweetAlert2](https://sweetalert2.github.io/ "Link to Sweet Alert 2 page")
     - SweetAlert2 was used to customise the **Contact Form** success message for UX 
- [Pagination](https://flask-paginate.readthedocs.io/en/master/ "Link to flask-paginate documentation")
     - `flask_paginate` extension was used to implement pagination functionality on select pages.
- [Jinja](http://jinja.pocoo.org/docs/2.10/ "Link to Jinja information")
     - Jinja templating language was used to simplify and display backend data in html.

### Database Management
- [SQLite](https://www.sqlite.org/index.html "Link to SQLite site")
     - SQLite was used as a single-file database during development.
- [Heroku Postgres](https://www.heroku.com/postgres "Link to Heroku Postgres site")
     - Heroku Postgres was used for production database, provided by Heroku.


[Back to top ⇧](#table-of-contents)

## Testing

Testing information can be found in a separate testing [file](TESTING.md "Link to testing file")

## Deployment
To further develop this project, a clone can be made using the following steps:
### 1. Database Creation


### 2. Local Copy Creation
A Local Clone of the repository can be made in two ways:

- **Forking the Repository:**

     By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

     1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     3. At the top of the repository, on the right side of the page, select "Fork".
     4. You should now have a copy of the original repository in your GitHub account.

-  **Creating a Clone**

     How to run this project locally:
     1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
     2. After installation, restart the browser.
     3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     5. Click the green "GitPod" button in the top right corner of the repository.
     This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

     How to run this project within a local IDE, such as VSCode:

     1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     3. Under the repository name, click "Clone or download".
     4. In the Clone with HTTPs section, copy the clone URL for the repository.
     5. In your local IDE open the terminal.
     6. Change the current working directory to the location where you want the cloned directory to be made.
     7. Type 'git clone', and then paste the URL you copied in Step 3.
     ```
     git clone https://github.com/USERNAME/REPOSITORY
     ```
     8. Press Enter. Your local clone will be created.

     (Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Link to GitHub troubleshooting"))

Once a local clone is created, the environment variables have to be set:

1. Create a `.gitignore` file in the project's root directory.
2. In the terminal window, type `touch env.py` to create the file that will contain the environment variables. 
3. Add `env.py` to the `.gitignore` file.
4. Within the `env.py` file, enter the project's environment variables:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", <your_secret_key>)
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority" )
os.environ.setdefault("MONGO_DBNAME", <your_mongo_db_name>)
```
For the `MONGO_URI` ensure to replace `<username>`, `<password>`, `<cluster_name>` and `<database_name>` with the appropriate alternatives.



### 3. Heroku App Creation
The website requires back-end technology, including a server, application and database. It is because of this that the project was deployed on **Heroku**, a container-based cloud Platform as a Service. There are two ways to deploy on Heroku:

- Using the Heroku Command Line Interface
- Connect to GitHub Repository (the developer recommends this method)

Before deployment can be carried out on Heroku, the following steps must be carried out:

1. Create a `requirements.txt` file to install all requirements. In the terminal window, type the following command:
```
pip3 install -r requirements.txt
```
2. Create a `Procfile` file so that Heroku knows which file runs the app. In the terminal window, type the following command:
```
echo web: python app.py > Procfile
```
*Remove the blank line that may occur at the end of the Procfile to avoid any issues*


3. Push the two files to the repository:
```
git add requirements.txt
git commit -m "Add requirements.txt"

git add Procfile 
git commit -m "Add Procfile"

git push
```
Once these steps are completed, continue with the process:

1. Log into [Heroku](https://id.heroku.com/login "Link to Heroku login page") or [create an account](https://signup.heroku.com/login "Link to Heroku sign-up page").
2. Select the `New` button on the top-right of the page, and choose `Create New App`. Give your app a unique name and set the region (in this instance: **Europe**). Then click `Create App`.
3. Navigate to the `Deploy` tab on the dashboard and select `Connect to GitHub`.
4. Search for the repository name (ensuring it is spelled correctly). Once located, click `Connect`. 
5. Navigate to the `Setting` tab on the dashboard and select `Reveal Config Vars`, entering the necessary key/values as below:

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000
SECRET_KEY | `<your_secret_key>`
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority`
MONGO_DBNAME | `<your_mongo_db_name>`

6. Navigate back to the `Deploy` tab and scroll down to `Automatic Deploys`.
7. Ensure that the `master` branch is selected, then select `Enable Automatic Deploys`.

Heroku will receive the pushed code from the GitHub repository and host the application with the required packages set out. 

The deployed version can now be viewed by selecting `View App` in the top-right of the page.


[Back to top ⇧](#table-of-contents)

## Credits 
The developer consulted multiple sites in order to better understand the code they needed to implement their deisgn. 

The [Code Institute Boutique Ado Mini Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1) was used as a reference point for the developer in the development of the core functionality of the website. The lessons included with the mini-project helped the developer to get a better understanding of each functionality and how to customise it to suit their project.

For code that was copied and edited, the developer made sure to reference this within the code. The following sites were used on a more regular basis:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [JSfiddle](https://jsfiddle.net/ "Link to JSfiddle page")

[Back to top ⇧](#table-of-contents)

## Acknowledgements
The developer would like to thank the following:

[Back to top ⇧](#table-of-contents)

***
