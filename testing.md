# Testing.

## HTML
[W3C Validator](https://validator.w3.org/) was used to test [HTML](https://www.w3schools.com/html) code to enure if passed certain criteria.


## CSS
[W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) used to check the [CSS](https://www.w3schools.com/Css) code to enure it passes certain criteria for a well functioning website.<br>


## Python
[Python Checker](https://www.pythonchecker.com/) help check code syntax and to keep to [PEP8](https://pep8.org) standards.<br>
![Pylint100%](media/readme-images/pylint100.png)<br>
Line of code too long for [PEP8](https://pep8.org) standards.<br>
![Long Line](media/readme-images/pylintlongline.png)<br>


This error below said that the '/' needed whitespace around the code, but it made the code incorrect so has been left.<br>
![Error left alone](media/readme-images/Pylinterror.png)<br>
Image of the template error with the spacing as suggested by Pylint [Python Checker](https://www.pythonchecker.com/).<br>
![Template error](media/readme-images/TemplateError.png)



## PEP 8 linter
[PEP8 CI](https://pep8ci.herokuapp.com/) with Code Institute to check [Python](https://www.python.org) code.<br>
PEP8 Packages can be installed in the coding environment. This image below shows the Linter not working as it should on the coding environemtn during this project.<br>
'Problems' tag remains with - no issues. Which definately was not the case. Other linter options are avaliable.<br>
![PEP8 error](media/readme-images/PEP8%26FLAKE8Check.png)
<br>

### Bookings App pylint checks.

[Python Checker](https://www.pythonchecker.com/) for Bookings / forms.py<br>
![Forms](/media/readme-images/PYBookingForms.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Bookings / admin.py<br>
![Admin](/media/readme-images/PYBookingAdmin.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Bookings / models.py<br>
![Models](/media/readme-images/PYBookingModels.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Bookings / views.py<br>
![Views](/media/readme-images/PYBookingViews.png)<br>
<hr>


### Forum App pylint checks.

[Python Checker](https://www.pythonchecker.com/) for Forum / forms.py<br>
![Forms](/media/readme-images/PYForumForms.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Forum / admin.py<br>
![Admin](/media/readme-images/PYForumAdmin.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Forum / models.py<br>
![Models](/media/readme-images/PYForumModels.png)<br>
<hr>

[Python Checker](https://www.pythonchecker.com/) for Forum / views.py<br>
![Views](/media/readme-images/PYForumViews.png)<br>
<hr>

### Test pylint for Bookings and Forum App.

## Tests
[Django Test Suite](https://docs.djangoproject.com/en/4.2/topics/testing/) can be used for tests to validate if code is working as expected.<br>
Tests can be ran by entering 'python filename.py test' in CLI on cloud coding development environment. For this project the CLI input was 'python manage.py test' and the coding environment was [Gitpod](https://www.gitpod.io).<br>
Test CLI.<br>
![Test CLI entry](media/readme-images/TestCLI.png)<br>
Passing tests example below.<br>
![Test Pass](media/readme-images/TestPass.png)<br>
Failing tests example below.<br>
![Test Failing](media/readme-images/TestFail.png)<br>

### Run tests from [Django Test Suite](https://docs.djangoproject.com/en/4.2/topics/testing/).
To run these tests, the Database Engine environment had to be changed from [ElephantSQL](https://www.elephantsql.com) environment to [SQlite3](https://sqlite.org).<br>
![Database Switch](media/readme-images/DBswitchTest.png)

[Back to the top](#testing)
<hr>