# Cocktail Bar

# BEANFEAST

# Fullstack Project - 4.

This project is based on a website with a booking system in a fictional setting. It has been created to portait a website where a user can create a booking at a cocktail bar named **Beanfeast** and then view, delete and cancel any bookings made.<br>
The user registers to the site first before being able to carry out a booking.<br>
Once registered they have access to the booking system and can also comment on a Forum created to inform user's of new Events, new cocktails or changes to the cocktail bar from the management site. The Discussion Board created for the website can be used to create discussions about certain topics in the Forum's, aswell as being able to 'like or unlike' a 'Forum Post' or 'Forum Comment'.<br>
The frontend of the website should encourage users to visit the website and booking, visit the cocktail bar itself, created discussions, offer ease of use and fictional contact information for any other queries.<br>
The management system has an Administraion page for backend user's of the site, so management or staff can access the bookings via Bookings Item page on Django Admin, approve bookings and comments, and create Event pages via the Forum Posting page. Comments can be made and seen here in the Django Admin to be approved here via the Forum Comment page.
<br>
<hr>

[Deployable Link to Project site.]()<br>

<hr>
<br>

![Responsive Desgin]()<br>

<br>


## Table of Contents.

* [User Experience](#user-experience)
* [Admin Experience](#admin-experience)
* [Admin Login](#)
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
They could be added to a ToDo list, In Progress list or Done status. User stories could be followed and changed. If time ran out for project progression, they could be adapted.<br>
Creation and progress of User Stories in Issues on [Github](https://github.com) example using a Kanban Board for viewing User Story image below.<br>
![Issues US](media/readme-images/IssuesUS.png)<br>
Projects can be created from the tabs menu. Along side Issues which can be attached the the repositories Project.<br>
![Project](media/readme-images/RepoPI.png)
<br>

The user experience offers features such as:
<ul>
<li>Registering to the website.</li>
<li>Sign out and Sign out options.</li>
<li>The home page offers information on upcoming events straight away. This is paginated to offer one Event/New item per page.</li>
<li>On click of the Forum Title, the next page offers full information on that Event or New snippet.</li>
<li>On click of the Forum Title, the next page offers a Discussion Board.</li>
<li>When logged in or registered, user's can comment of Forum Posts.</li>
<li>When logged in or registered, user's can delete their comment on the Forum Posts.</li>
<li>When logged in or registered, user's like or unlike Forum Posts.</li>
<li>User's can see how many likes and comments a Forum Post has.</li>
<li>Users can make booking, edit bookings and cancel them too.</li>
<li>Users can view these bookings on a separate page once it is approved</li>
<li>User receives <em>pop up</em> messages to inform them of their actions.</li>
<li>Users can view social links. (For fictional state, all social links are connected to a homepage for that said socail site)</li>
<li>Users can see the opening times and days in the footer. (Fictional times and days)</li>
<li>Users can see the <em>last orders</em> call too.(Fictional last orders)</li>
<li>Users can see an address and contact information.(Fictional address and contact information)</li>
</ul>


# Admin Experience.

Django was used to create an Administraion panel Interface that has information from both the 'Bookings' App and 'Forum' App, directed to it for staff and management to receive and manipulate. See [Other Installed Libaries](#other-installed-libaries) for more information on creating and starting new projects and applications with Django.
<br>
The installed applications should be added to **INSTALLED_APPS in settings.py**. See example below.<br>

![Installed apps](media/readme-images/InApp.png)<br>

<br>

In Beanfeast project, within the directory, a url path has to be added to `url.py` and imported from Django:<br>
![URL path](media/readme-images/URLandImport.png)<br>

Verify that Admin has be installed but migrating additions. See [migrations](#migrations) for more details on migrating.<br>

Create a **superuser** to use the administraion page. Not avaliable to just anybody!<br>

CLI input **python3 manage.py createsuperuser**.<br>
Follow the instructions to enter:<br>
USERNAME:<br>
EMAIL:(NOT NEEDED)<br>
PASSWORD:<br>
<br>
Login panel, if it is working looks like the below image:<br>

![Log in](media/readme-images/DjangoAdminLogin.png)<br>

The models being used now need to be registered with the Admin panel.<br>
Register is and connect it to a class, inside the `admin.py` file for the App.<br>
Make sure django.contrib imports admin.<br>
![Admin to class](media/readme-images/DjangoAdminRegister.png)<br>

View in Django Admin once registered, below.<br>
BOOKINGS = Application name.<br>
Items = Model for booking items.<br>
![Model in Admin](media/readme-images/ModelinAdmin.png)<br>

Or simpley register it, inside the `admin.py` file for the App.<br>
![Admin alone](media/readme-images/DjangoAdminReg.png)<br>

Once the models are registered, they can be accessed via Django Admin.<br>

To access the admin site the following context should be used:<br>
`http://your-server-ip:8000/admin`<br>
The `username` created for the purpose of this website is:
The `password` created for the purpose of this website is:

The administraion experience offers features such as:
<ul>
<li>View forum in draft or published stage.</li>
<li>View bookings or forum posts by whether they have been approved or not.<br>

![AproveYN](media/readme-images/ApproveYN.png)</li>

<li>Add Forum posts and Forum comments from Admin.</li>
<li>Can add images to the Forum post itself.</li>
<li>Approve or delete a booking.</li>
<li>Approve or delete comments.</li>
<li>Events/News that have been created in Forum can be removed. They are viewed one per page.<br>
Improves user focus on one Forum post.</li>
</ul>
<br>

[Back to the top](#cocktail-bar)

<hr>

# Agile

The Agile Tool used to develop this project was on Github's Project Board. A Project can be added to a repository, and then Issues can be built up from here to make a todo list, in progress list or done list. These Issues can carry 'User Stories', to create separate categories such as importment, could do, done or not done. User Stories can be broken down into many more catergories. Templates for Issues can be edited and created to suit certain needs, such as 'User Stories' for this project.<br>

Filled in Template for Issues.<br>
![User Story Template](media/readme-images//USFull.png)<br>

Issues can be added to todo list, in progress list or done list. They can also be added to a Repository(Project 4).<br>
![Added to project Todo List](media/readme-images/USConnect.png)<br>

Labels can be created or use default labels to organise the Issues relating to the Project Board.<br>
![Labels Use](media/readme-images/USDoneandNotdone.png)<br>
<br>

[Back to the top](#cocktail-bar)
<hr>

# MVC framework.

The **MVC framework** needs to be followed to ensure models can be used, viewed and controlled to implement software constructs using three main components. <em>Model, View</em> and <em>Controller.</em><br>


## Model

A 'model' is created within a class, in `models.py`.<br>
The 'model' is to create the ability to check reservations and approve them.<br>
![MVC model](media/readme-images/MVCModel.png)<br>

## View

That model is placed into a class to create a 'view', in `views.py`.<br>
It gets all the objects from the reservation 'model', applys any requirements and sets a request for rendering HTML to a 'view'.<br>
![MVC view](media/readme-images/MVCView.png)<br>

URL Patterns are created with class and function names from the models.<br>

## Controller

When the 'view' is modelled, it creates a 'controller' accessible feature to update the model, as in this example.<br>
The staff or management can receive the booking and approve or delete it.<br>
![MVC controller](media/readme-images/MVCController.png)<br>
<br>

[Back to the top](#cocktail-bar)

<hr>

# Design

## Colours

Colour Scheme for the website is based on a very tasty cocktail - Amaretto Sour. With light and deep orangey colours, an egg white topping and a red cherry on top.<br>
Black is always got for an outline or to ensure writing stands out.<br>
![Colours](media/readme-images/Colours.png)<br>


## Typography

The fonts were used from [Google Fonts](https://fonts.google.com/) and are install by  link in the Head of the page.<br>
Bebas Neue - I like the large capital block type use of this font with contrast well with the funky more 'fruity' floaty font type of the Yellowtail. <br>
Oswald - This was a good business standard text to use and very readable, like the Bebas Neue.<br>
Yellowtail - This 'fruitier' messy style i thought, suited a Cocktail Bar style, for the text.<br>
<br>

## Icons

Icons are created by [Font Awesome](https://fontawesome.com/) and used in this project. They are used to portait social links, a pulsing 'Heart' icon on the Bookings page and a different 'Heart' icon again for the like status. Also, a speech bubble is used for the 'Total number of comments' icon.
<br>

[Back to the top](#cocktail-bar)

<hr>


# Features.

This projects **Features**, for a potentail cocktail bar called **Beanfeast** includes:
<br>

**Navigation Bar** - Contains Logo, a little excerpt and navigation links. User can login, register, sign out and navigate back to home page.<br>
Home page has access to the Forums.<br>

![Nav Bar](media/readme-images/FeaturesNav.png)<br>
<br>
**When viewed on a smaller device, the Nav Bar shrinks.**<br>
![Small Nav](media/readme-images/NavSmall.png)<br>

**Welcome page** - Welcome to Beanfeast message and link to Forum's upcoming Events and News.<br>

![HOME](media/readme-images/Fhome.png)
<br>
<br>
**Bookings page** - For Booking Form view.<br>
<br>
**Register and Login Page** - User can login in or register in not done so already.<br>

![Login](media/readme-images/Login.png)
<br>
<br>
**Log Out Page** - Once logged in, a 'Sign out' page will be avaliable.<br>

**View Bookings page** - on 'VIEW NOW' page.<br>

**Booking Form** - send a booking request to Admin for approval via a form requesting, name, email, date, time, number of people and a radio button to tick for 'HAPPY TO AWAIT APPROVAL'.<br>

![booking Form](media/readme-images/BookingForm.png)<br>

**Date** - Select a date in the format YYYY-MM-DD.<br>

**Time** - Select a time in the format HH-MM-SS.<br>

**Create a booking.** - once created the user has to wait for approval from 'admin' before they are viewed and confirmed. This could potentailly help with tables or times being double booked if the 'admin' can confirm it as an avaliable booking slot.<br>

**View bookings.** - once approved. The user will be able to view their bookings, once logged in, from the website on the 'VIEW NOW' page. They will be able to edit and cancel bookings from here. All forms have a background-image of a cocktail.<br>
![View Booking example](media/readme-images/FeaturesApproved.png)
<br>
<br>
**No Bookings** - No Bookings.<br>
![No bookings](media/readme-images/NoBookings.png)
<br>
<br>
**Edit current bookings.** - The user can edit their bookings and again, have to wait for approval for the booking to be viewed and accepted by 'admin' side.<br>

**Cancel or Delete a booking.** - Bookings can be fully removed. It a user cancels a booking, the booking will be removed from the 'admin' side also.<br>

**Register** - The user need to register to the site before being able make a booking.<br>
<br>
<br>
**Forum Post for Events** - Administraion can post events occuring at the Cocktail Bar. User's registered to the website will be able to comment on these Events. Unregistered user's to the website will be able to see the 'Event' information of the Forum but not be able to comment.<br>

**Forum Comments for Event** - Regitered User's will be able to comment on Event posting's. They will be viewed on the website if Administraion has approved it. This offers a discussion board for user's of the website.<br>

![Forum Page](media/readme-images/Forum.png)

**Delete Comments** - A user can delete a comment they have posted if they are signed in.<br>
<br>

**If user is not signed in, comments can not be deleted.**<br>

![Can not delete](media/readme-images/DeleteCommentNotAuth.png)

<br>

**If user is signed in, comments can be deleted.**<br>

![Can delete](media/readme-images/DeleteCommentAuth.png)
<br>
<br>
**User needs to be authenticated via** [Jinja](https://jinja.palletsprojects.com) IF statement.<br>

![User Auth](media/readme-images/DeleteCommentHtml.png)


**Likes** - 'Likes' can be clicked and are represented as a 'heart icon' for people, again, who are registered can 'like' a comment or Event posting. A user can choose to 'unlike' a post too by re-clicking the 'heart icon'.<br>
![Heart Icon](media/readme-images/HeartIcon.png)

**Images** - Different images can be displayed for each different Forum Post created. An image is also displayed in the forms background.<br>
<br>
**Footer** - Has social links, opening times and days, a fictioncal contact number and address.<br>
![Footer](media/readme-images/FeaturesFooter.png)<br>

**Alert Banners** - As the user interacts with the webpage, such as registering, creating a booking, editing a booking or cancelling one, 'Alert Banners' through 'Message Tags in Django' are created as prompts.
<br>

**JavaScript** - Used to set time out for alert banners. Created with Code Institute walkthrough projects.

Input into settings.py
![Setting Message Tags](media/readme-images/MessageTags.png)<br>

These had to be written into settings.py and have a for loop created for them to loop 'message' and then the 'tag'. Such as 'message.success'.<br>
<br>
**Csrf Token** - Included in forms for protection of user information in form submissions.<br>
![CSRF](media/readme-images/csrf.png)<br>

**Input into HTML in [Jinja](https://jinja.palletsprojects.com) For Loop.**<br>
![HTML message tags](media/readme-images/MessageTagsForLoop.png)<br>

<hr>

[Back to the top](#cocktail-bar)<br>

<hr>

# Deployment

To deploy this Full Stack project, [Heroku](https://dashboard.heroku.com/), a cloud based platform was used.
Follow the steps for deployment method:<br>
1. If needed, sign in and register to Heroku website first. _Click_ on **New** in the top right corner to create a new application. <br>
![Pic 1](media/readme-images/Heroku.png)<br>

2. Add an application name. Follow the rules of what you can enter. Select a region, and _click_ **Create App**.<br>
![Pic 2](media/readme-images/Heroku2.jpeg)<br>
3. Next stage will be a few changes on this page below. First, click into **Settings**.
![Pic 3](media/readme-images/Heroku3.3.png.jpeg)<br>
4. Once in **Settings**, Config Vars need altering. Remove <em>DISABLE_COLLECTSTAIC</em> on deployment.<br>
![Pic 4](media/readme-images/HerokuConfig.png)<br>
**ALSO**<br>
<em>DEBUG</em> in settings.py need to be set to <em>FALSE</em> for deployment.<br>
5. Now _click_ into **Deploy**. This wesbite was connected to **Github**. Which can be selected at the top. The **orange line**, shows the location to connect your repository from **Github** to **Heroku**. _Enter_ the name of the repository you need and connect. This pictures shows the repository already connected via **Github**. _Scroll_ to the bottom of the page to deploy. Select **main branch** and _click_ **Deploy Branch**.<br>
![Pic 5](media/readme-images/Heroku5.5.png.jpeg)<br>
6. The website may show as _building_ for a while. Once it has completed, it should look like the images below, with a **view** link. _Click_ here to view your website.<br>
![pic 6](media/readme-images/Heroku6.png)<br>

[Back to the top](#cocktail-bar)

<hr>

## Clone website.

To clone the project. I _clicked_ **code** in the respository file. In the dropdown menu, **copy** the link.<br>
Here, on the image below,  the locations are highlighted in **pink**.<br>
![clone](media/readme-images/cloneFS.png)<br>
Once cloned, **open** an IDE such as **GitBash**, to clone your wesbite. _Type_ **git clone** followed by your copied **URL link**. Hit enter.
![git clone for git bash](media/readme-images/cloneFS2.png)<br>

[Back to the top](#cocktail-bar)<br>

<hr>

# Technologies Used.

This content includes the variety of Technologies used in creating this website to make it function and to improve the development, aesthetics, functionality and compatability.<br>
<br>

# Installing Django.

## Django

This project has implemented [Django](https://www.djangoproject.com/), a [Python](https://www.python.org/) web framework. [Django](https://www.djangoproject.com/) has been used it different ways to help build this site.<br>

[Django](https://www.djangoproject.com/) frameworks and API's used are as followed:
[Messages Tags.](https://django.readthedocs.io/en/stable/ref/contrib/messages.html)<br> to create Alert banners for particular user actions.<br>
[Administration](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/) for Admin Interface Model.<br>
[Testing](https://docs.djangoproject.com/en/4.2/topics/testing/) built in while building website when creating a [Django](https://www.djangoproject.com/) Project.<br>
[Allauth](https://django-allauth.readthedocs.io/en/latest/) was used as a Django application to created authentication, account management and registration.<br>
<br>
<br>

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

## Font Awesome

[Font Awesome](https://fontawesome.com) Used for icons. Used direct through the [Font Awesome](https://fontawesome.com) website or via a [Bootstrap CDN](https://www.bootstrapcdn.com/) link.<br>

<br>

[Back to the top](#cocktail-bar)

<br>
<hr>

# Other Installed Libaries.

## Requirements.txt file.

A file was created within the project to hold all the necessary input for these installed libaries to function - **requirements.txt**.<br>
![Requirements.txt file](media/readme-images/RequirementsFile.png)<br>

### REQUIRED FILE.

Redirect to requirement.txt to store the files when installation is successfull.

CLI input - **pip3 freeze --local > requirements.txt**.<br>
<br>
### SERVER GUNICORN

To run [Django](https://www.djangoproject.com/) on, for [Heroku](https://dashboard.heroku.com/) devlopment.

CLI input - **pip3 install 'django<4' gunicorn**.<br>
<br>

### POSTGRESQL LIBARY - ELEPHANTSQL.

[ElephantSql](https://www.elephantsql.com/) hosted the Database for storing data to be used within a cloud.

CLI input - pip3 install dj_database_url==0.5.0 psycopg2.<br>
<br>

### CLOUDINARY CLOUD STORAGE.

This was used to store images for use within the project. Other files can be hosted here too.<br>

CLI input - **pip3 install dj3-cloudinary-storage**.<br>
<br>


### NEW DJANGO PROJECT.

Creates new manage.py file and a directory called 'beanfeast'.<br>

CLI input - **django-admin startproject beanfeast .** (dot(.) = create project in current directory)<br>
<br>


### CREATE FORUM AND BOOKINGS APP (NEW APP).

Creates a new application within the project with separate files for manpulating.

CLI input - **python3 manage.py startapp forum** (add to settings.py file. INSTALLED_APPS).<br>
CLI input - **python3 manage.py startapp bookings** (add to settings.py file. INSTALLED_APPS).<br>
<br>

### DJNAGO SUMMERNOTE.

[Summernote](https://summernote.org/getting-started/) uses the Open Source libraries jQuery and Bootstrap.

CLI input - **pip install django-summernote**
<br>
<br>

### DJANGO CRISPY FORMS.

[Django Crispy Form Template](https://pypi.org/project/django-crispy-forms/) is used to build reusable layouts out of components, can editor HTML without the HTML content in the template.<br>

CLI input - **pip install django-crispy-forms**
<br>
<br>

## Django Alluth

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) is used to create pages to register on, sign in and sign out and help support authernication flow on the website.<br>

CLI input - **pip3 install django-allauth**
<br>
<br>

### MIGRATE CHANGES

To migrate to the Database for each new App or change to App.<br>

CLI input - **python3 manage.py migrate** <br>
<br>

### RUN SERVER 

CLI input -- **python3 manage.py runserver**<br>
(IF URL NOT ALLOWED - ADD URL TO ALLOWED_HOSTS in settings.py).<br>
<br>

### NON-COMMITED FILE

A file called **env.py** should be created to hold environments for safely developing new websites.<br>
It should be entered into the .gitignore file to avoid being commited.<br>
This does involve saving a snippet of it incase the coding environment is closed and returned to at a later date, and a new environment is created. **The env.py is not saved**.<br>
![Env.py file](media/readme-images/Env.png)
<hr>

**Snippet**<br>

import os<br>
<br>
os.environ["DATABASE_URL"]="postgres-URL-here"<br>
os.environ["SECRET_KEY"]="ooh-super-secret"<br>
os.environ["CLOUDINARY_URL"] ="cloudinary-URL-here"<br>
<br>

[Back to the top](#cocktail-bar)

<hr>

<br>

## Migrations.

As models are created they have to be migrated to the Database. New models or even edited or changed models.<br>
CLI input:<br>


#### Check which migrations are to be made.

**python3 manage.py makemigrations --dry-run**<br>  
<br>

#### To make the migrations shown.

**python3 manage.py makemigrations**<br>
<br>

#### To show any migrations that need to be done in a list, for indentification.

**python3 manage.py showmigrations**<br>
<br>

![Show migrations](media/readme-images/MigrateShow.png)<br>
<br>
#### To complete the migration.

**python3 manage.py migrate**<br>

![Migration example](media/readme-images/migrate.png)<br>

[Back to the top](#cocktail-bar)

<hr>

<br>


## Jinja.

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
Confirmation of booking with the cocktail bar, rather then having to log in to check if it has been approved from the website 'VIEW NOW' page.<br>
<br>
When a booking is 'rejected', the user view for the user will display the **You have no bookings with us yet...** message. This could be confirmed better, even via email.<br>
<br>
Implementing a choice of date, by supplying a widget or different input format, possibly from Django.forms.Form.<br>
Bookings could be displayed in sections to show the user awaiting approval, approved and not approved status.<br>
<br>
In a real world situation, a Cocktail Bar would have a limited number of tables each hour, on each day. This could be greatly improved so Admin would not have to reject so many booking requests, as they probably would with this website.<br>
<br>
For this project, tables fit a max of 10 people with no minimum. Anybody welcome!<br>
This could mean sitting 5 groups of 2 at a table of 10 to fill up the cocktail bar.<br>
Hoping for adaptable users!<br>
In the future different table sizes could be created to suit different groups of people.<br>
Over booking and double booking tables would be important to avoid. The Admin or management for this project can just reject the bookings, but in the future a better approach can be developed.<br>
<br>

I would have liked to offer the users a separate Gallery and Menu pages so they could see the Cocktails avaliable and see what Beanfeast the Cocktail Bar itself looked like before arriving. This would have greatly increase User Experience to this site.<br>
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

5. [Python Testing Documents](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual) for testing tips.

6. [Bloomreach](https://documentation.bloomreach.com/engagement/docs/jinja-syntax) for checking Jinja methods.

[Back to the top](#cocktail-bar)

<hr>


# Awknowledgements.
To the **Tutor Support** team for [Code Institute](https://codeinstitute.net/) for continued support and assitance.<br>
To mentor **Precious Ijege** for continued support and patience while taking part in the course provided by [Code Institute](https://codeinstitute.net/) for a Diploma in Full Stack Software Development.<br>
To the Walkthrough projects of both <em>'Hello Django'</em> and <em>'I think therefore I blog'</em> mini projects supplied by [Code Institute](https://codeinstitute.net/) Coursework.<br>

<hr>

[Back to the top](#cocktail-bar)

<hr>
