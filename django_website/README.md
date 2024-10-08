# Django project using Python
This is a example Python Django project for my personal understanding of how to create a Django blog web application.

Original content creator is: 
https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1

## Initial Installation
Install the following packages via your terminal assuming you have python and pip installed.
```bash
python -m pip install Django
```
```bash
pip install numpy
```
```bash
pip install django-crispy-forms
```
```bash
pip install crispy-bootstrap5
```
## Running application
To run the application run the following command in your project location where manage.py is located.
```bash
python manage.py runserver
```

## Other Django commands
Create a new app within the project
```bash
python manage.py startapp blog
```
Implements changes made to the application. E.g. new tables created.
```bash
python manage.py makemigrations
```
Created a superuser so that they can login to the Admin page.
```bash
python manage.py createSuperUser
```

## Passwords
| Username | Password |
|----------|----------|
| dlarkin | password |
| TestUser | TestPassword |

## Creating a Python Virtual Environment
```bash
pip3 install virtualenv
virtualenv env_django
.\env_django\bin\activate
```