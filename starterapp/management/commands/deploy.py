import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        os.system('heroku create')
        os.system('git add .')
        os.system('git rm starterapp/management/commands/generate.py')
        os.system("git commit -m 'first commit to heroku'")
        os.system('git push heroku master')
        os.system('heroku run python manage.py syncdb')
        os.system('heroku run python manage.py migrate')
