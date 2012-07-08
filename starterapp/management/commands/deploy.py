import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #os.system('heroku create')
        import ipdb; ipdb.set_trace()
        os.system('git add .')
        os.system("git commit -m 'first commit to heroku'")
        os.system('git push heroku master')
        os.system('heroku run python manage.py syncdb')
        os.system('heroku run python manage.py migrate')
