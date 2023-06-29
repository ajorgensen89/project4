# Testing.


## HTML

[W3C Validator](https://validator.w3.org/) was used to test [HTML](https://www.w3schools.com/html) code to enure if passed certain criteria.

<hr>


## CSS

[W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) used to check the [CSS](https://www.w3schools.com/Css) code to enure it passes certain criteria for a well functioning website.<br>
[Bootstrap CSS](https://getbootstrap.com/) was also used to create elements of [CSS](https://www.w3schools.com/Css).
All my CSS created within static/css/style.css can be navigated to and viewed under validated CSS<br>
![Validated CSS Nav](media/testing-images/ValidatedCSSTitle.png)<br>
Validated CSS shows all my CSS within the static/css/style.css file.<br>
![CSS](media/testing-images/ValidatedCSS.png)<br>
<br>
<hr>


## Python

[Python Checker](https://www.pythonchecker.com/) help check code syntax and to keep to [PEP8](https://pep8.org) standards.<br>
![Pylint100%](media/testing-images/pylint100.png)<br>
Line of code too long for [PEP8](https://pep8.org) standards.<br>
![Long Line](media/testing-images/pylintlongline.png)<br>


This error below said that the '/' needed whitespace around the code, but it made the code incorrect so has been left.<br>
![Error left alone](media/testing-images/Pylinterror.png)<br>
Image of the template error with the spacing as suggested by Pylint [Python Checker](https://www.pythonchecker.com/).<br>
![Template error](media/testing-images/TemplateError.png)

<hr>


## PEP 8 linter

[PEP8 CI](https://pep8ci.herokuapp.com/) with Code Institute to check [Python](https://www.python.org) code.<br>
<br>
PEP8 Packages can be installed in the coding environment. This image below shows the Linter not working as it should, on the coding environment during this project.<br>
'Problems' tag remains with - no issues. Which definately was not the case. Other linter options are avaliable.<br>
![PEP8 error](media/testing-images/PEP8%26FLAKE8Check.png)
<br>


### Bookings App pylint checks.

[Python Checker](https://www.pythonchecker.com/) for Bookings / forms.py<br>
![Forms](/media/testing-images/PYBookingForms.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Bookings / admin.py<br>
![Admin](/media/testing-images/PYBookingAdmin.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Bookings / models.py<br>
![Models](/media/testing-images/PYBookingModels.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Bookings / views.py<br>
![Views](/media/testing-images/PYBookingViews.png)<br>
<hr>


### Forum App pylint checks.

[Python Checker](https://www.pythonchecker.com/) for Forum / forms.py<br>
![Forms](/media/testing-images/PYForumForms.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Forum / admin.py<br>
![Admin](/media/testing-images/PYForumAdmin.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Forum / models.py<br>
![Models](/media/testing-images/PYForumModels.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Forum / views.py<br>
![Views](/media/testing-images/PYForumViews.png)<br>
<hr>


## Test pylint for Bookings and Forum App.

To run the [Django Test Suite](https://docs.djangoproject.com/en/4.2/topics/testing/) TestCase, the Database needs changing.
**For normal code developement, use Database:**<br>
![Normal DB](media/testing-images/RunDB.png)<br>
**When tesing with Django TestCase, use Database:**<br>
![Testing DB used](media/testing-images/RunDBTest.png)<br>


## Test in Django - TestCase

[Django Test Suite](https://docs.djangoproject.com/en/4.2/topics/testing/) has a built-in testing framework that can be used for tests to validate if code is working as expected using **TestCase**.<br>
Tests can be ran by entering 'python filename.py test' in CLI on cloud coding development environment. For this project the CLI input was 'python manage.py test' and the coding environment was [Gitpod](https://www.gitpod.io).<br>
**Test CLI.**<br>
![Test CLI entry](media/testing-images/TestCLI.png)<br>
**Passing tests example below.**<br>
![Test Pass](media/testing-images/TestPass.png)<br>
**Failing tests example below.**<br>
![Test Failing](media/testing-images/TestFail.png)<br>


## Run tests from [Django Test Suite](https://docs.djangoproject.com/en/4.2/topics/testing/) with TestCase.

To run these tests, the Database Engine environment had to be changed from [ElephantSQL](https://www.elephantsql.com) environment to [SQlite3](https://sqlite.org).<br>
![Database Switch](media/testing-images/DBswitchTest.png)
<br>

<hr>
<br>


## Coverage.

Coverage can be installed and ran to see that percentage of tests covering a website.
![Coverage](media/testing-images/Coverage.png)

Coverage commands to install and run a report.
![Coverage CLI](media/testing-images/CoverageCLI.png)

<br>
[Back to the top](#testing)

<hr>

[Back to README.md](README.md)

<hr>