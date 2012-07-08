# Purpose
This will create a Django project for you that is already built with a landing page with login and a logged in homepage. The templates use Twitter Boostrap CSS and JS. You can also deploy directly to Heroku in the same one line.

# Dependencies
* pip
* virtualenv
* a (free) Heroku account (https://api.heroku.com/signup)
* Heroku Toolbelt (https://toolbelt.herokuapp.com/)

# Create your project
First, decide your project name (i.e. coolproject) amd the path where you want your project to live (i.e. /Users/cooldude/Documents/MyProjects/)

Download django-buddy and in the root directory (which has manage.py), run the following command

```
python manage.py generate --path='/Users/cooldude/Documents/MyProjects/' --name='coolproject'
```

The script will prompt you to create a superuser for the database, which is SQLite.

The script will create a virtual environment, install dependencies, sync the db, do an initial South migration and initialize a git repository.

Finally, it will runserver on localhost:8000.

# Create your project AND deploy all in one line
Note that you need to install Heroku toolbelt (above in Dependencies), but that's it!


## Instantly create and deploy:
```
python manage.py generate --path='/Users/cooldude/Documents/MyProjects/' --name='coolproject' --deploy
```

## Deploy after creating:
First, generate the project without `--deploy`. Modify the project however you like until you're ready to deploy it. Then just run
```
python manage.py deploy
```

When deploying, you will be prompted to create a superuser for your Heroku hosted database in exactly the same way as it would happen for local.


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
      home.html - basic home page after having logged in
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