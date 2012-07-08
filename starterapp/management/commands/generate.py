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
        self.plant_seed(**kwargs)
        self.install()
        self.sync_and_runserver()
        if kwargs.get('deploy'):
            self.deploy()

    def plant_seed(self, **kwargs):
        source = os.getcwd()
        # This is hacky but okay for now
        destination = kwargs.get('path')
        if destination[len(destination) - 1] != '/':
                destination = '{}/'.format(destination)
        if kwargs.get('name'):
                destination = '{}{}'.format(destination, kwargs.get('name'))

        print "Copying seed project to {}...".format(destination)
        shutil.copytree(source, destination)
        os.chdir(destination)
        print os.getcwd()

        os.system('find . -name "*.pyc" -exec rm -rf {} \;')
        os.system('find . -name "default_db" -exec rm -rf {} \;')
        os.system('rm starterapp/management/commands/generate.py')

    # def generate_active_settings(self):
    #     f = open(os.getcwd() + '/settings/active.py', 'w+')
    #     f.write('LOCAL = True\n')
    #     f.write('def get_env():\n')
    #     f.write('    return LOCAL\n')
    #     f.close()

    def install(self):
        print "Installing virtualenv with distribute..."
        os.system('virtualenv venv --distribute')
        print "Installing requirements..."
        os.system('pip install -r requirements.txt')
        print "Syncing db..."

    def sync_and_runserver(self):
        os.system('python manage.py syncdb')
        print "Running initial South migration..."
        os.system('python manage.py migrate')
        print "Initializing git repo"
        os.system('git init')
        print "Running server at 127.0.0.1:8000....."
        os.system('python manage.py runserver')

    def deploy(self):
        os.system('heroku create')
        os.system('git add .')
        os.system("git commit -m 'first commit to heroku")
        os.system('git push heroku master')
        os.system('heroku run python manage.py syncdb')
        os.system('heroku run python manage.py migrate')
