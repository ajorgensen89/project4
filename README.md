# Cocktail Bar
# BEANFEAST
# Fullstack Project - 4.
This project is based on a website with a booking system in a fictional setting. It has been created to portait a website where a user can create a booking at a cocktail bar named **Beanfeast** and then view, delete and cancel any bookings made.
The user registers to the site first before being able to carry out a booking.
Once registered they have access to the booking system and can also comment on a Forum created to inform user's of new Events, new cocktails or changes to the cocktail bar from the management site. The Discussion Board created for the website can be used to create discussions about certain topics in the Forum's, aswell as being able to 'like or unlike' a 'Forum Post' or 'Forum Comment'.
The frontend of the website should encourage users to visit the website and booking, visit the cocktail bar itself, created discussions, offer ease of use and fictional contact information for any other queries.
The management system has an Administraion page for backend user's of the site, such as management or staff can access the bookings via Bookings Item page, approve bookings and comments, and create Event pages via the Forum Posting page. Comments can be made and seen to be approved here via the Forum Comment page.
<br>
<hr>

[Deployable Link to Project site.]()<br>
<hr>
<br>

![Responsive Desgin]()<br>
<br>


## Table of Contents.

* [User Experience](#user-experience)
* [Flow Chart](#flow-chart)
	- [Creative writing](#creative-writing)
* [Features](#features)
* [Testing](testing.md)
* [Clone Website](#clone-website)
* [Technologies](#technologies)
* [Deployment](#deployment)
* [Credits](#credits)
* [Awknowledgements](#awknowledgements)
<br>

# User Experience
## Responsive Design.
[Ai I responsive?](https://ui.dev/amiresponsive) was used to check its look on a number of different devices and responsiveness. The text should be instructive but not too long, that viewing becomes difficult on mobile devices.<br>
![Responsive Desgin]()<br>

<hr>

## User Stories
User Stories were created to build the website from particular needs and requirements for this type of 'booking style' website.<br>
User Stories were created on [Github](https://github.com) respository as a Project which could have 'Issues' added to work on.<br>
They could be added to a ToDo list, In Progress list or Done status. User stories could be followed and changed. If time ran out, they could be adapted.<br>
Creation and progress of User Stories in Issues on [Github](https://github.com) example using a Kanban Board for viewing User Story image below.<br>
![Issues US](media/readme-images/IssuesUS.png)<br>
Projects can be created from the tabs menu. Along side Issues which can be attached the the repositories Project.<br>
![Project](media/readme-images/RepoPI.png)
<br>

## Agile
The Agile Tool used to develope this project was on Github's Project Board. A Project can be added to a repository, and then Issues can be built up from here to develop steps of ToDo list, In Progress list or Done status. These Issues can carry 'User Stories' and can be created into separate categories such as importment, could do, done or not done. User Stories can be broken down into many more catergories. Templates for Issues can be edited and created to suit certain needs, such as 'User Stories' for this project.<br>

Filled in Template for Issues.<br>
![User Story Template](media/readme-images//USFull.png)<br>

Issues can be added to todo list, in progress list or done list. They can also be added to a Repository(Project 4).<br>
![Added to project Todo List](media/readme-images/USConnect.png)<br>

Labels can be created or used default labels to organise the Issues relating to the Project Board.<br>
![Labels Use](media/readme-images/USDoneandNotdone.png)<br>
<br>

## Colours

## Typography
The fonts were used from [Google Fonts](https://fonts.google.com/) and are install by  link in the Head of the page.<br>
Bebas Neue - I like the large capital block type use of this font with contrast well with the funky more 'fruity' floaty font type of the Yellowtail. <br>
Oswald - This was a good business standard text to use and very readable, like the Bebas Neue.<br>
Yellowtail - This 'fruitier' messy style i thought, suited a Cocktail Bar style for the text.<br>
<br>

## Icons
Icons are created by [Font Awesome](https://fontawesome.com/) and used in this project. They are used to portait social links, a pulsing 'Heart' icon on the Bookings page and a different 'Heart' icon again for the like status. Also, a speech bubble is used for the 'Total number of comments' icon.
<hr>
<br>

[Back to the top](#cocktail-bar)

<hr>

# Features.
This projects **Features**, for a potentail cocktail bar called **Beanfeast** includes:
**Navigation Bar** - Contains Logo, a little excerpt and navigation links.<br>
![Nav Bar](media/readme-images/FeaturesNav.png)<br>
**Welcome page** - Welcome to Beanfeast message and link to Forum's and upcoming Events and News.<br>
**Bookings page** - For Booking Form view.<br>
**Register and Login Page** - User can login in or register in not done so already.<br>
**Log Out Page** - Once logged in, a 'Sign out' page will be avaliable.<br>
**View Bookings page** - on 'VIEW NOW' page.<br>
**Booking Form** - send a booking request to Admin for approval via a form requesting, name, email, date, time, number of people and a radio button to tick for 'HAPPY TO AWAIT APPROVAL'.<br>
![booking Form](media/readme-images/BookingForm.png)<br>
**Date** - Select a date in the format YYYY-MM-DD.<br>
**Time** - Select a time in the format HH-MM-SS.<br>
**Create a booking.** - once created the user has to wait for approval from 'admin' before they are viewed and confirmed. This could potentailly help with tables or times being double booked if the 'admin' can confirm it as an avaliable booking slot.<br>
**View bookings.** - once approved. The user will be able to view their bookings, once logged in, from the website on the 'VIEW NOW' page. They will be able to edit and cancel bookings from here. All forms have a background-image of a cocktail.<br>
![View Booking example](media/readme-images/FeaturesApproved.png)

**No Bookings** - No Bookings.<br>
![No bookings](media/readme-images/NoBookings.png)

**Edit current bookings.** - The user can edit their bookings and again, have to wait for approval for the booking to be viewed and accepted by 'admin' side.<br>
**Cancel or Delete a booking.** - Bookings can be fully removed. It a user cancels a booking, the booking will be removed from the 'admin' side also.<br>
**Register** - The user need to register to the site before being able make a booking.<br>

**Forum Post for Events** - Administraion can post events occuring at the Cocktail Bar. User's registered to the website will be able to comment on these Events. Unregistered user's to the website will be able to see the 'Event' information of the Forum but not be able to comment.<br>
**Forum Comments for Event** - Regitered User's will be able to comment on Event posting's. They will be viewed on the website if Administraion has approved it. This offers a discussion board for user's of the website.<br>
**Likes** - 'Likes' can be clicked and are represented as a 'heart icon' for people, again, who are registered can 'like' a comment or Event posting. A user can choose to 'unlike' a post too by re-clicking the 'heart icon'.<br>
**Images** - Different images can be displayed for each different Forum Post created. An image is also displayed in the forms background.<br>
**Footer** - Has social links, opening times and days, a fictioncal contact number and address.<br>
![Footer](media/readme-images/FeaturesFooter.png)<br>

**Alert Banners** - As the user interacts with the webpage, such as registering, creating a booking, editing a booking or cancelling one, 'Alert Banners' through 'Message Tags in Django' are created as prompts.<br>

Input into settings.py
![Setting Message Tags](media/readme-images/MessageTags.png)<br>

Input into HTML in [Jinja](https://jinja.palletsprojects.com) For Loop.<br>
![HTML message tags](media/readme-images/MessageTagsForLoop.png)<br>

These had to be written into settings.py and have a for loop created for them to loop 'message' and then the 'tag'. Such as 'message.success'.<br>
**Csrf Token** - Included in forms for protection of user information in form submissions.<br>
![CSRF](media/readme-images/csrf.png)<br>

<hr>

[Back to the top](#cocktail-bar)<br>

<hr>

# Deployment
To deploy for a Full Stack website, [Heroku](https://dashboard.heroku.com/), a cloud based platform was used.
Follow the steps for deployment method.<br>
1. If needed, sign in and register to Heroku website first. _Click_ on **New** in the top right corner to create a new application. <br>
![Pic 1]()<br>

2. Add an application name. Follow the rules of what you can enter. Select a region, and _click_ **Create App**.<br>
![Pic 2]()<br>
3. Next stage will be a few changes on this page below. First, click into **Settings**.
![Pic 3]()<br>
4. Once in **Settings**, Config Vars need adding. Change the _KEY and VALUE_ headings. In this case to _PORT and 8000_. Other files such as _creds.json_ file would be added here.<br>
Now add buildpacks. _Click_ buildpack to choose. It this instance, two, python and nodejs where added. They can be rearranged and deleted if needed here.<br>
**Important - python needs to be on top**. <br>
![Pic 4]()<br>
5. Now _click_ into **Deploy**. This wesbite was connected to **Github**. Which can be selected at the top. The **orange line**, shows the location to connect your repository from **Github** to **Heroku**. _Enter_ the name of the repository you need and connect. This pictures shows the repository already connected via **Github**. _Scroll_ to the bottom of the page to deploy. Select **main branch** and _click_ **Deploy Branch**.<br>
![Pic 5]()<br>
6. The website may show as _building_ for a while. Once it has completed, it should look like the images below, with a **view** link. _Click_ here to view your website.<br>
![pic 6]()<br>

[Back to the top](#cocktail-bar)

<hr>

## Clone website.
To clone the project. I _clicked_ **code** in the respository file. In the dropdown menu, **copy** the link.<br>
Here, on the image below,  the locations are highlighted in **pink**.<br>
![clone](images/readme-images/clone.png)<br>
Once cloned, **open** an IDE such as **GitBash**, to clone your wesbite. _Type_ **git clone** followed by your copied **URL link**. Hit enter.
![git clone for git bash](images/readme-images/clone2.png)<br>

[Back to the top](#cocktail-bar)<br>

<hr>

# Technologies Used
This content includes the variety of Technologies used in creating this website to make it function and to improve the development, aesthetics, functionality and compatability.<br>
# Installing Django

## [Django](https://www.djangoproject.com/)
This project has implemented [Django](https://www.djangoproject.com/), a [Python](https://www.python.org/) web framework. [Django](https://www.djangoproject.com/) has been used it different ways to help build this site.

[Django](https://www.djangoproject.com/) frameworks and API's used are as followed:
[Messages Tags.](https://django.readthedocs.io/en/stable/ref/contrib/messages.html)<br> to create Alert banners for particular user actions.<br>
[Administration](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/) for Admin Interface Model.<br>
[Testing](https://docs.djangoproject.com/en/4.2/topics/testing/) built in while building website when creating a [Django](https://www.djangoproject.com/) Project.<br>
[Allauth](https://django-allauth.readthedocs.io/en/latest/) was used as a Django application to created authentication, account management and registration.<br>

## Font Awesome
[Font Awesome](https://fontawesome.com) Used for font text. Used direct through the [Font Awesome](https://fontawesome.com) website or via a [Bootstrap CDN](https://www.bootstrapcdn.com/) link.<br>

## Bootstrap
[Bootstrap](https://getbootstrap.com/) was downloaded into the coding workspace by a [Bootstrap CDN](https://www.bootstrapcdn.com/) to be used throughout the website for inbuilt solutions and methods for helping the layout and design of this website including, style, colour, formatting and poistioning.<br>
Here are a few links to different areas of the Bootstrap wesbite that was used within this website.<br>
Here's some examples of Bootstrap that were used:<br>
[CSS grid](https://getbootstrap.com/docs/4.0/layout/grid/) with [Bootstrap](https://getbootstrap.com/)<br>
[CSS colours](https://getbootstrap.com/docs/4.0/utilities/colors/) with [Bootstrap](https://getbootstrap.com/)<br>
[CSS colouring](https://www.bitdegree.org/learn/bootstrap-colors)<br>
[Bootstrap Icons](https://www.bootstrapcdn.com/bootstrapicons/)<br>
[Bootstrap Cards](https://getbootstrap.com/docs/4.0/components/card/)<br>
[Bootstrap Buttons](https://getbootstrap.com/docs/4.0/components/buttons)<br>
[Bootstrap CSS](https://getbootstrap.com/docs/4.1/layout/grid/)<br>
<br>

## Crispy Forms
[Django Crispy Form Template](https://pypi.org/project/django-crispy-forms/) used to render HTML.<br>

## Summernote
[Summernote](https://summernote.org/getting-started/) has been imbedded into [Django](https://www.djangoproject.com/) to improve the layout for administraion input.<br>
<br>

## Python Tutor.
[Python PEP8 checker](https://www.pythonchecker.com/). Helps to test, run and visualize parts of code to pass PEP8 requirements.<br>
<br>

## Heroku.
[Heroku](https://dashboard.heroku.com/) is a cloud based platform used to deploy the application on.<br>
<br>

## Github.
[Github](https://github.com/) was used to edit and build the website using  code.<br>

<br>

[Back to the top](#cocktail-bar)

<br>
<hr>

# Other Installed Libaries.

## Requirements.txt file
A file was created within the project to hold all the necessary input for these installed libaries to function - **requirements.txt**.<br>
![Requirements.txt file](media/readme-images/RequirementsFile.png)<br>

### SERVER GUNICORN
To run [Django](https://www.djangoproject.com/) on, for [Heroku](https://dashboard.heroku.com/) devlopment.

CLI input - **pip3 install 'django<4' gunicorn**.<br>

### POSTGRESQL LIBARY - ELEPHANTSQL

CLI input - pip3 install dj_database_url==0.5.0 psycopg2.<br>

### CLOUDINARY CLOUD STORAGE

CLI input - **pip3 install dj3-cloudinary-storage**.<br>

### REQUIRED FILE > redirect to requirement.txt to store the files when installation is successfull

CLI input - **pip3 freeze --local > requirements.txt**.<br>

### NEW DJANGO PROJECT 

CLI input - **django-admin startproject beanfeast .** (dot(.) = create project in current directory)<br>

Creates new manage.py file and a directory called 'beanfeast'.<br>

### CREATE FORUM AND BOOKINGS APP (NEW APP)

CLI input - **python3 manage.py startapp forum** (add to settings.py file. INSTALLED_APPS).<br>
CLI input - **python3 manage.py startapp bookings** (add to settings.py file. INSTALLED_APPS).<br>

### DJNAGO SUMMERNOTE
[Summernote](https://summernote.org/getting-started/) uses the Open Source libraries jQuery and Bootstrap.

CLI input - **pip install django-summernote**
<br>

### DJANGO CRISPY FORMS
[Django Crispy Form Template](https://pypi.org/project/django-crispy-forms/) is used to build reusable layouts out of components, can editor HTML without the HTML content in the template.<br>

CLI input - **pip install django-crispy-forms**
<br>

## Django Alluth
[Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) is used to create pages to register on, sign in and sign out and help support authernication flow on the website.<br>

CLI input - **pip3 install django-allauth**
<br>

### MIGRATE CHANGES

CLI input - **python3 manage.py migrate** (To migrate to the Database for each new App or change to App.<br>

### RUN SERVER 

CLI input -- **python3 manage.py runserver**<br>
(IF URL NOT ALLOWED - ADD TO ALLOWED_HOSTS in settings.py).<br>

### NON-COMMITED FILE
A file called **env.py** should be created to hold environments for safely developing new websites.<br>
It should be entered into the .gitignore file to avoid being commited.<br>
This does involve saving a snippet of it incase the coding environment is closed and returned to at a later date, and a new environment is created. **The env.py is not saved**.<br>
![Env.py file](media/readme-images/Env.png)
<hr>
import os<br>
<br>
os.environ["DATABASE_URL"]="postgres://bhmjznxq:ITITqbyVtRT4T9kr2mrh0dkiEg3oCZRT@rogue.db.elephantsql.com/bhmjznxq"<br>
os.environ["SECRET_KEY"]="aj_^secret@key_is_this"<br>
os.environ["CLOUDINARY_URL"] ="cloudinary://526811634986951:vRc66sG5CkpCnHRqaN33bLo_4-0@dtsaa4qbs"<br>
<br>

[Back to the top](#cocktail-bar)

<hr>
<br>

## Migrations
As models are created they have to be migrated to the Database. New models or even edited or changed models.
CLI input:<br>
#### Check which migrations are to be made.
**python3 manage.py makemigrations --dry-run**<br>  
#### To make the migrations shown.
**python3 manage.py makemigrations**<br>
#### To show any migrations that need to be done in a list, for indentification.
**python3 manage.py showmigrations**<br>

![Show migrations](media/readme-images/MigrateShow.png)<br>

#### To complete the migration.
**python3 manage.py migrate**<br>
![Migration example](media/readme-images/migrate.png)<br>

[Back to the top](#cocktail-bar)

<hr>
<br>

## Jinja
[Jinja](https://jinja.palletsprojects.com) Python template engine was used within this project in input blocks of code. IF/ELSE statements can also be created depending on what template or [HTML](https://en.wikipedia.org/wiki/HTML) needs rendering to the view.<br>
Example of **Block content** in jinja templating highlighted in **yellow box**<br>
Example of **If/Else** in jinja templating highlighted in **purple box**<br>
Example of **For loop** in jinja templating highlighted in **green box**.<br>
Example of **empty** in jinja templating highlighted in **brown box**. This show HTML is nothing is rendered to the page.<br>
![If/else example](/media/readme-images/Jinja.png)<br>

<hr>
[Back to the top](#cocktail-bar)
<hr>
<br>
<hr>

# Browser combatability.
Checked the websites combatability with the following browers:
1. Apple Safari.
2. Google Chrome.
3. Opera Browser.
4. Microsoft Edge.<br>

Ran the website with no significant issues.<br>

<hr>

See [Testing](testing.md) file for full use of technologies used to test this wesbite.<br>

[Back to the top](#cocktail-bar)

<hr>

# Future Features and business logic.
This project could benefit from a number of diffferent features in the future. Due to time and skill constraints, some could not be implemented. Some future features are just fresh ideas that the website could benefit from in a real world situation.<br>
<br>
Email's could be sent to the user to confirm whether they received a booking with the cocktail bar, rather then having to log in to check if it has been approved from the website 'VIEW NOW' page.<br>
Different emails could be changed or registered with the account.<br>
<br>
Bookings could be displayed in sections to show the user awaiting approval, approved and not approved status.<br>
In a real world situation, a Cocktail Bar would have a limited number of tables and could only post certain tables at each hour, on each day. This could be greatly improved so the Admin not not have to reject so many booking requests, as they probably would with this website.<br>
For this porject, tables can be booked up to a max of 10 people with no minimum. Anybody welcome! This could mean sitting 5 groups of 2 at a table of 10 to fill up the cocktail bar. Hoping for adaptable users!<br>
In the future different table sizes could be created to suit different groups of people.<br>
Over booking and double booking tables would be important to avoid. The Admin or management for this project can just reject the bookings, but in the future a better approach can be developed on top on what has been created.<br>
<br>
I would have liked to offer the users a separate Gallery and Menu pages so they could see the Cocktails avaliable and see what Beanfeast the Cocktail Bar itself looked like before arriving. This would have greatly increase User Experience to this site.
<br>
The Agile Tool, for this instance, was Github Project Boards, can label Issues and User Stories that have not been completed and would offer a good starting ground for future development and features for this project, Beanfeast site.<br>
Template of Not Done labelled Issue.<br>
![Template of Not done](media/readme-images/USAdminNotDone.png)<br>

'Not Done' labelled items can be filtered out on the Project Board.<br>
![Filter Not Done](media/readme-images/USFilterNotDone.png)<br>

<br>

[Back to the top](#cocktail-bar)

<hr>

# Credits.

1. [Code Institute](https://codeinstitute.net/) for providing examples of [Django](https://www.djangoproject.com/) projects through [Code Institute](https://codeinstitute.net/) Coursework to grasp the concept of building projects using databases, multiple libaries, API's, frameworks, Bootstrap, Django and Django Built-in benefits such as testing. This helped when creating my 'Booking App' and 'Forum' App and applying migrations to database of installed items. It also helped with the use of [Bootstrap CSS](https://getbootstrap.com/docs/4.1/layout/grid/) use. <br>
It also helped with the creation of 'Message Tags'.<br>

2. [Stack Overflow](https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django). for help with authenticating user using [Django](https://www.djangoproject.com/) methods.<br>

3. [Django Documents](https://docs.djangoproject.com/en/4.2/topics/testing/overview/) for testing using TestCase.

4. [Django Documents](https://docs.djangoproject.com/en/4.2/topics/testing/advanced/) Testing tips and hints.
<br>

5. [Bloomreach](https://documentation.bloomreach.com/engagement/docs/jinja-syntax) for checking Jinja methods.

[Back to the top](#cocktail-bar)

<hr>

# Awknowledgements.
To the **Tutor Support** team for [Code Institute](https://codeinstitute.net/) for continued support and assitance.<br>
To mentor **Precious Ijege** for continued support and patience while taking part in the course provided by [Code Institute](https://codeinstitute.net/) for a Diploma in Full Stack Software Development.<br>
To the Love Sandwiches 'Example project' for Python code supplied by Anna Greaves, Content Developer for [Code Institute](https://codeinstitute.net/).<br>

<hr>

[Back to the top](#cocktail-bar)

<hr>
