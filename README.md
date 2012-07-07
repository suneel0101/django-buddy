# Purpose
This will create a Django project for you that is already built with a landing page with login and a logged in homepage. The templates use Twitter Boostrap CSS and JS.

# Dependencies
pip, virtualenv

# Create your project
1. Select the destination where you want your project to live, i.e. /Users/cooldude/Documents/MyProjects/
2. Select your project name
3. Download django-buddy and in the root directory (which has manage.py), run the following command
`python manage.py generate --path='/Users/cooldude/Documents/MyProjects/' --name='coolproject'`
4. The script will prompt you to create a superuser for the database, which is SQLite
5. The script will create a virtual environment, install dependencies, sync the db, do an initial South migration and initialize a git repository.
6. Finally, it will runserver on localhost:8000.

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
![Screenshot of landing page](https://github.com/suneel0101/django-buddy/raw/master/images/landing_page.png)
## Logged in homepage
![Screenshot of logged in homepage](https://github.com/suneel0101/django-buddy/raw/master/images/home_page.png)
## Admin
![Screenshot of admin](https://github.com/suneel0101/django-buddy/raw/master/images/django-admin.png)