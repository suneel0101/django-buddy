import shutil
import os
import sys
from optparse import make_option

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-p", "--path", type="string", dest="path", default=None, help='Path to folder'),
        make_option("-n", "--name", type="string", dest="name", default=None, help='Name of project'),
        make_option('--deploy', action='store_true', dest='deploy', default=False, help="Deploys to Heroku."),
        make_option("-a", "--app", type="string", dest="app", default=None, help='Name of app'),
    )

    def handle(self, *args, **kwargs):
        self.plant_seed(**kwargs)
        self.app_name = kwargs.get('app')
        if self.app_name:
            self.rename_app()
        self.install()
        print "Syncing local copy of your app..."
        self.sync_local()
        if kwargs.get('deploy'):
            print "!!!!!!!!!!!!!!! DEPLOYING TO HEROKU !!!!!!!!!!!!!!!!!!"
            self.deploy()
            print "Your app is now live! Check it out!"
        else:
            print "Your app is setup at {}".format(self.destination)

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
        f = open(destination + '/settings/local.py', 'w+')
        f.close()
        print "Installing requirements..."
        os.system('pip install -r requirements.txt')
        os.chdir(destination)
        print os.getcwd()

        os.system('find . -name "*.pyc" -exec rm -rf {} \;')
        os.system('find . -name "default_db" -exec rm -rf {} \;')
        os.system('rm starterapp/management/commands/generate.py')

        self.destination = destination

    def rename_app(self, **kwargs):
        views = self.destination + '/urls.py'
        settings = self.destination + '/settings/__init__.py'
        self.replace_app_name_in_file(views)
        self.replace_app_name_in_file(settings)
        os.system("mv starterapp {}".format(self.app_name))

    def replace_app_name_in_file(self, path_to_file):
        _file = open(path_to_file, 'r')
        lines = _file.readlines()
        _file.close()

        _newfile = open('tmpfile.py', 'w+')
        for line in lines:
            _newfile.write(line.replace("starterapp", self.app_name))
        _newfile.close()

        os.system('rm {}'.format(path_to_file))
        os.system('mv tmpfile.py {}'.format(path_to_file))

    def install(self):
        print "Installing virtualenv with distribute..."
        os.system('virtualenv venv --distribute')
        print "Installing requirements..."
        os.system('pip install -r requirements.txt')
        print "Syncing db..."

    def sync_local(self):
        print "Initializing git repo"
        os.system('git init')

    def runserver(self):
        os.system('python manage.py runserver')

    def deploy(self):
        os.system('heroku create')
        os.system('git add .')
        os.system('git rm starterapp/management/commands/generate.py')
        os.system("git commit -m 'first commit to heroku'")
        os.system('git push heroku master')
        os.system('heroku run python manage.py syncdb')
        os.system('heroku run python manage.py migrate')
