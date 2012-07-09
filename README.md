# Purpose
Setting up and deploying a project is always a huge hassle.
But not anymore! With DjangoBuddy, in just one line you can generate a skeleton app and deploy it to Heroku!

# What you get
* landing page, home page and Django admin
* built-in authentication based on Django auth
* templates that use Twitter Bootstrap CSS and JS
* standard Django app files populated with the necessary import statements
* ONE COMMAND that generates and deploys your app

# Before you start
There are just a few easy and quick steps to take before you are on your way to an awesome and live site!

1. If you don't have it, install pip (http://pypi.python.org/pypi/pip/)
2. Make sure you have virtualenv (http://pypi.python.org/pypi/virtualenv/). You can just do ```pip install virtualenv```.
3. Signup for a (free) Heroku account (https://api.heroku.com/signup)
4. Download the Heroku Toolbelt (https://toolbelt.herokuapp.com/)

# Get started
Choose your project name (i.e. coolproject) and the path where you want your project to live (i.e. /Users/cooldude/Documents/MyProjects/)


1. `git clone git://github.com/suneel0101/django-buddy.git`
2. `heroku login`
(You will be prompted to enter your Heroku username and password.)
3. `cd django-buddy `
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`


# Create and deploy your project
There are two main options.

1. Generate the app and deploy it all in one command.
2. Generate the app, modify it and then deploy it.

## Case 1: Generate and deploy all in one command
```
python manage.py generate --path='/Users/cooldude/Documents/MyProjects/' --name='coolproject' --deploy
```

The script will prompt you to create a superuser for the local database.
Then, it will deploy to Heroku and ask you to create a superuser for the live database.


## Case 2: Create, modify and then deploy:
```
python manage.py generate --path='/Users/cooldude/Documents/MyProjects/' --name='coolproject'
```
Then,

1. `cd /Users/cooldude/Documents/MyProjects/coolproject`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

Modify the project however you like until you're ready to deploy it. 
Then,
```
python manage.py deploy
```

# Project Structure:
```
project_name /
   starter_app/
        views, admin, models, management commands
   media/
        css/
           twitter bootstrap css
        js/
           twitter bootstrap js
   templates/
      base.html  - template base
      login.html - basic landing page with login functionality
      home.html - basic logged in home page
   settings/
      settings.py
      You can add different local/dev/staging/production settings files in the settings module
```

# What it looks like
## Landing page
![Screenshot of landing page](https://github.com/suneel0101/django-buddy/raw/master/media/img/landing_page.png)
## Logged in homepage
![Screenshot of logged in homepage](https://github.com/suneel0101/django-buddy/raw/master/media/img/home_page.png)
## Admin
![Screenshot of admin](https://github.com/suneel0101/django-buddy/raw/master/media/img/django-admin.png)