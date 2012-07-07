import shutil
import os
from optparse import make_option

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-p", "--path", type="string", dest="path", default=None, help='Path to folder'),
        make_option("-n", "--name", type="string", dest="name", default=None, help='Name of project'),
    )

    def handle(self, *args, **kwargs):
        source = os.getcwd()
        destination = kwargs.get('path') + kwargs.get('name')
        print "Copying seed project to {}...".format(destination)
        shutil.copytree(source, destination)
        os.chdir(destination)
        print os.getcwd()
        os.system('find . -name "*.pyc" -exec rm -rf {} \;')
        os.system('find . -name "default_db" -exec rm -rf {} \;')
        os.system('rm starterapp/management/commands/generate.py')
        print "Installing virtualenv with distribute..."
        os.system('virtualenv venv --distribute')
        print "Installing requirements..."
        os.system('pip install -r requirements.txt')
        print "Syncing db..."
        os.system('python manage.py syncdb')
        print "Running initial South migration..."
        os.system('python manage.py migrate')
        print "Initializing git repo"
        os.system('git init')
        print "Running server at 127.0.0.1:8000....."
        os.system('python manage.py runserver')
