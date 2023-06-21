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
* [Game Features](#game-features)
* [Trial and Errors](#trial-and-errors)
* [Testing](testing.md)
* [Clone Website](#clone-website)
* [Credits](#credits)
* [Technologies](#technologies)
     - [Module](#module)
* [Deployment](#deployment)
* [Credits](#credits)
* [Awknowledgements](#awknowledgements)
<br>

# User Experience

<br>

### Steps
Some steps and ideas to take when building this project.<br>
![Ideas](images/readme-images/Basictemplate.png)<br>

<hr>

### Business logic.


<hr>

## Responsive Design.
[Ai I responsive?](https://ui.dev/amiresponsive) was used to check its look on a number of different devices and responsiveness. The text should be instructive but not too long, that viewing becomes difficult on mobile devices.<br>
![Responsive Desgin](images/readme-images/AiIResp.png)<br>

<hr>

# Flow Chart.
## Lucid Chart.
I used [Lucid Chart](https://www.lucidchart.com/pages/) to create a flow chart of how to create a battleship game.
1. Start - welcome message
2. User name input - raises an error if no input is submitted and loops untill there is input.
3. Select Battleship position (Not on chart - added later.)
4. Select Row:Column for grid - Select the numbers between 0-4 for both row and column. The input should be validated if guessed before or invalid. You would have to try again.
5. Check if used before. Re-select.
6. Loop untill AI or user wins.
7. Option to restart game or exit.
<br>
![Lucid Chart](images/readme-images/LucidChart.png)<br>

[Back to the top](#battleship-game-created-for-python-project)

<hr>

# Game Features.

## Hit.<br>


![HIT image](images/readme-images/HITexample.png)<br>

## Missed and battleship location.<br>


![MISSED image](images/readme-images/MISSEDexample.png)<br>

## Location already tried.<br>

![ALREADY MISSED](images/readme-images/AiandPreg.png)<br>
<br>
<br>
![FIRST TRY](images/readme-images/IFalready.png)<br>
<br>
![SECOND TRY](images/readme-images/Xalready.png)<br>
<br>
<br>
<br>
![FINAL CODE USED](images/readme-images/XalreadyFix.png)<br>


## End of game.<br>



![GAME OVER](images/readme-images/WinandStopgame.png)<br>

## Name<br>



The AI's board is also distinguished with a title.<br>
![NAME](images/readme-images/NAMEfeature.png)<br>

## Guess row and column. <br>


![RC prompt](images/readme-images/RCprompt.png)<br>

## Placing Battleships<br>

<br>
![SHIP Placement](images/readme-images/Battle.png)<br>

## Turn counter<br>


![Tally](images/readme-images/TurnCount.png)<br>


## Validating input.<br>


To see how this was tested click to view the [Testing](testing.md) file here.<br>

## Restart game.<br>



<hr>

## Future Features.<br>




[Back to the top](#battleship-game-created-for-python-project)

<hr>

# Trial and errors. <br>

### APPENDING LISTS<br>


### WRONG RANDOM NUMBER GENERATED.<br>

![Range error](images/readme-images/ERRORrun.png)<br>



<hr>

## Known Error.<br>



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

## [Python](https://www.python.org/)
This project has been coded in [Python](https://www.python.org/) language.

## Module.
Imported for use in this website was __randomint__ from the random module <br>

## Font Awesome
[Font Awesome](https://fontawesome.com)

## Bootstrap
[Bootstrap]() was downloaded into the coding workspace by a [Bootstrap CDN](https://www.bootstrapcdn.com/) to be used throughout the website for inbuilt solutions and methods for helping the layout and design of this website including, style, colour, formatting and poistioning. Here are a few links to different areas of the Bootstrap wesbite that was used within this website.
Here's some examples of Bootstrap that were used.

## Crispy Forms
[Django Crispy Form Template](https://pypi.org/project/django-crispy-forms/) used to render HTML.



[CSS colouring](https://www.bitdegree.org/learn/bootstrap-colors)
[Bootstrap Icons](https://www.bootstrapcdn.com/bootstrapicons/)
[Bootstrap Cards](https://getbootstrap.com/docs/4.0/components/card/)
[Bootstrap Buttons](https://getbootstrap.com/docs/4.0/components/buttons)
[Bootstrap](https://getbootstrap.com/docs/4.1/layout/grid/)

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

2. []() for validating input and providing an example python project through [Code Institute](https://codeinstitute.net/).<br>

3. [RtoDto.net.](). Better handling.

4. [Stack Overflow]() restart game tips. Adapted to suit this website.

5. [Stack Overflow](https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django). for help with authenticating user using Django methods.<br>

[Back to the top](#battleship-game-created-for-python-project)

<hr>

# Awknowledgements.
To the **Tutor Support** team for [Code Institute](https://codeinstitute.net/) for continued support and assitance.<br>
To mentor **Precious Ijege** for continued support and patience while taking part in the course provided by [Code Institute](https://codeinstitute.net/) for a Diploma in Full Stack Software Development.<br>
To the Love Sandwiches 'Example project' for Python code supplied by Anna Greaves, Content Developer for [Code Institute](https://codeinstitute.net/).<br>

<hr>

[Back to the top](#)

<hr>
