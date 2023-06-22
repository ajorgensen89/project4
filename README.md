# Cocktail Bar
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
	- [Lucid Chart](#lucid-chart)
* [Features](#features)
* [Testing](testing.md)
* [Clone Website](#clone-website)
* [Technologies](#technologies)
* [Deployment](#deployment)
* [Credits](#credits)
* [Awknowledgements](#awknowledgements)
<br>

# User Experience

<br>

<hr>

### Business logic.


<hr>

## Responsive Design.
[Ai I responsive?](https://ui.dev/amiresponsive) was used to check its look on a number of different devices and responsiveness. The text should be instructive but not too long, that viewing becomes difficult on mobile devices.<br>
![Responsive Desgin](images/readme-images/AiIResp.png)<br>

<hr>

[Back to the top](#battleship-game-created-for-python-project)

<hr>

# Features.


[Back to the top](#)<br>

<hr>

# Deployment
To deploy for a [Python](https://www.python.org/) language coded website, [Heroku](https://dashboard.heroku.com/), a cloud based platform was used.
Follow the steps for deployment method.<br>
1. If needed, sign in and register to Heroku website first. _Click_ on **New** in the top right corner to create a new application. <br>
![Pic 1](images/readme-images/Heroku.png)<br>

2. Add an application name. Follow the rules of what you can enter. Select a region, and _click_ **Create App**.<br>
![Pic 2](images/readme-images/Heroku2.jpeg)<br>
3. Next stage will be a few changes on this page below. First, click into **Settings**.
![Pic 3](images/readme-images/Heroku3.png.jpeg)<br>
4. Once in **Settings**, Config Vars need adding. Change the _KEY and VALUE_ headings. In this case to _PORT and 8000_. Other files such as _creds.json_ file would be added here.<br>
Now add buildpacks. _Click_ buildpack to choose. It this instance, two, python and nodejs where added. They can be rearranged and deleted if needed here.<br>
**Important - python needs to be on top**. <br>
![Pic 4](images/readme-images/Heroku4.png.jpeg)<br>
5. Now _click_ into **Deploy**. This wesbite was connected to **Github**. Which can be selected at the top. The **orange line**, shows the location to connect your repository from **Github** to **Heroku**. _Enter_ the name of the repository you need and connect. This pictures shows the repository already connected via **Github**. _Scroll_ to the bottom of the page to deploy. Select **main branch** and _click_ **Deploy Branch**.<br>
![Pic 5](images/readme-images/Heroku5.png.jpeg)<br>
6. The website may show as _building_ for a while. Once it has completed, it should look like the images below, with a **view** link. _Click_ here to view your website.<br>
![pic 6](images/readme-images/Heroku6.png)

<hr>

## Clone website.
To clone the project. I _clicked_ **code** in the respository file. In the dropdown menu, **copy** the link.<br>
Here, on the image below,  the locations are highlighted in **pink**.<br>
![clone](images/readme-images/clone.png)<br>
Once cloned, **open** an IDE such as **GitBash**, to clone your wesbite. _Type_ **git clone** followed by your copied **URL link**. Hit enter.
![git clone for git bash](images/readme-images/clone2.png)<br>

[Back to the top](#)<br>

<hr>

# Technologies

## [Django](https://www.djangoproject.com/)
This project has implemented [Django](https://www.djangoproject.com/), a [Python](https://www.python.org/) web framework. [Django](https://www.djangoproject.com/) has been used it different ways to help build this site.

[Django](https://www.djangoproject.com/) frameworks and API's used are as followed:
[Messages Tags.](https://django.readthedocs.io/en/stable/ref/contrib/messages.html)<br> to create Alert banners for particular user actions.<br>
[Administration](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/) for Admin Interface Model.<br>
[Testing](https://docs.djangoproject.com/en/4.2/topics/testing/) built in while building website when creating a [Django](https://www.djangoproject.com/) Project.<br>
[Allauth](https://django-allauth.readthedocs.io/en/latest/) was used as aDjango application to created authentication, account management and registration.<br>

## Font Awesome
[Font Awesome](https://fontawesome.com) Used for font text. Used direct through the [Font Awesome](https://fontawesome.com) website or via a [Bootstrap CDN](https://www.bootstrapcdn.com/) link.

## Bootstrap
[Bootstrap](https://getbootstrap.com/) was downloaded into the coding workspace by a [Bootstrap CDN](https://www.bootstrapcdn.com/) to be used throughout the website for inbuilt solutions and methods for helping the layout and design of this website including, style, colour, formatting and poistioning. Here are a few links to different areas of the Bootstrap wesbite that was used within this website.
Here's some examples of Bootstrap that were used:
[CSS grid](https://getbootstrap.com/docs/4.0/layout/grid/) with [Bootstrap](https://getbootstrap.com/)<br>
[CSS colours](https://getbootstrap.com/docs/4.0/utilities/colors/) with [Bootstrap](https://getbootstrap.com/)<br>

## Crispy Forms
[Django Crispy Form Template](https://pypi.org/project/django-crispy-forms/) used to render HTML.

## Summernote
[Summernote](https://summernote.org/getting-started/) has been imbedded into [Django](https://www.djangoproject.com/) to improve the layout for administraion input.

[CSS colouring](https://www.bitdegree.org/learn/bootstrap-colors)
[Bootstrap Icons](https://www.bootstrapcdn.com/bootstrapicons/)
[Bootstrap Cards](https://getbootstrap.com/docs/4.0/components/card/)
[Bootstrap Buttons](https://getbootstrap.com/docs/4.0/components/buttons)
[Bootstrap CSS](https://getbootstrap.com/docs/4.1/layout/grid/)

## Python Tutor.
[Python Tutor](https://pythontutor.com/visualize.html). Helps to test, run and visualize parts of code.

## Heroku.
[Heroku](https://dashboard.heroku.com/) is a cloud based platform used to deploy the application on.

## Github.
[Github](https://github.com/) was used to edit and build the website using  code.

# Broswer combatability.
Checked the websites combatability with the following browers:
1. Apple Safari.
2. Google Chrome.
3. Opera Browser.
4. Microsoft Edge.<br>

Ran the website with no significant issues.<br>

<hr>

See [Testing](testing.md) file for full use of technologies used to test this wesbite.<br>

[Back to the top](#)

<hr>

# Credits.

1. [Codecadmey](). I ran through and completed this example of building the battleship game code on this website provided. It had useful prompts and helped improve my understanding to create the code for the website.<br>

2. [Code Institute](https://codeinstitute.net/) for providing examples of [Django](https://www.djangoproject.com/) projects through [Code Institute](https://codeinstitute.net/) Coursework. This helped when creating my 'Forum' App. It also helped with the use of [Bootstrap CSS](https://getbootstrap.com/docs/4.1/layout/grid/) use. <br>

3. [RtoDto.net.](). Better handling.

4. [Youtuber](https://www.youtube.com/watch?v=2CXY_AKNdfk) for tips while using messages from [Django](https://www.djangoproject.com/).

5. [Stack Overflow](https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django). for help with authenticating user using [Django](https://www.djangoproject.com/) methods.<br>

[Back to the top](#battleship-game-created-for-python-project)

<hr>

# Awknowledgements.
To the **Tutor Support** team for [Code Institute](https://codeinstitute.net/) for continued support and assitance.<br>
To mentor **Precious Ijege** for continued support and patience while taking part in the course provided by [Code Institute](https://codeinstitute.net/) for a Diploma in Full Stack Software Development.<br>
To the Love Sandwiches 'Example project' for Python code supplied by Anna Greaves, Content Developer for [Code Institute](https://codeinstitute.net/).<br>

<hr>

[Back to the top](#)

<hr>
