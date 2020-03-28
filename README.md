# Login and signup with google recaptcha

The project demonstrate the more secure symtem for user registration on web application.

If someone from the same IP address attempts to register more than 3 times in a day,
they should be presented with a captcha (Google Recaptcha). The captcha should be
validated for all subsequent attempts to register for that IP address.

Database used to store the data is MongoDB

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

* Insatll a MongoDB on your system
* Install Python on your system
* Install Django on your system
```
pip install django
```
* Install Djongo on your system
```
pip install djongo
```
## Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be
* make changes in the settings.py file to localize the databse

```python
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'djongo', 
        'NAME': 'signup', # Change the name of the databes which you have created in mongo db compass
        
    }
}
```

* To make a superuser run the commnd in the directory where manage.py file is there
```
python manage.py createsuperuser
```
* To save all changes to the database run two more commands
```
python manage.py makemigrations
```
```
python manage.py migrate
```
* See the tables in the MongoDb in your datbase

## Start using

* start the local server
```
python manage.py runserver
```
Go to the local server and it will work


