import shutil
import os
from optparse import make_option

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-p", "--path", type="string", dest="path", default=None, help='Path to folder'),
        make_option("-n", "--name", type="string", dest="name", default=None, help='Name of project'),
        make_option('--deploy', action='store_true', dest='deploy', default=False, help="Deploys to Heroku."),
    )

    def handle(self, *args, **kwargs):
        self.plant_seed(**kwargs)
        self.generate_requirements()
        self.install()
        print "Syncing local copy of your app..."
        self.sync_local()
        #self.setup_gitignore()
        if kwargs.get('deploy'):
            print "!!!!!!!!!!!!!!! DEPLOYING TO HEROKU !!!!!!!!!!!!!!!!!!"
            self.deploy()
            print "Your app is now live! Check it out!"
        else:
            print "Running local server..."
            self.runserver()

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
        print "Installing requirements..."
        os.system('pip install -r requirements.txt')
        os.chdir(destination)
        print os.getcwd()

        os.system('find . -name "*.pyc" -exec rm -rf {} \;')
        os.system('find . -name "default_db" -exec rm -rf {} \;')
        os.system('rm starterapp/management/commands/generate.py')

    def generate_requirements(self):
        f = open(os.getcwd() + '/requirements.txt', 'w+')
        f.write('Django==1.4\n')
        f.write('distribute==0.6.24\n')
        f.write('psycopg2==2.4.5\n')
        f.write('wsgiref==0.1.2\n')
        f.write('MySQL-python==1.2.3\n')
        f.write('gunicorn==0.14.2\n')
        f.write('South==0.7.4\n')
        f.write('dj-database-url==0.2.0\n')
        f.close()

    def install(self):
        print "Installing virtualenv with distribute..."
        os.system('virtualenv venv --distribute')
        print "Installing requirements..."
        os.system('pip install -r requirements.txt')
        print "Syncing db..."

    # def setup_gitignore(self):
    #     f = open(os.getcwd() + '/.gitignore', 'w+')
    #     f.write('*.pyc\n')
    #     f.write('venv/*\n')
    #     f.write('default_db\n')
    #     f.write('.DS_Store\n')
    #     f.write('active.py\n')
    #     f.close()

    def sync_local(self):
        os.system('python manage.py syncdb')
        print "Running initial South migration..."
        os.system('python manage.py migrate')
        print "Initializing git repo"
        os.system('git init')

    def runserver(self):
        os.system('python manage.py runserver')

    def deploy(self):
        os.system('heroku create')
        os.system('git add .')
        # Hacky, TODO: make it less hacky
        os.system('git rm starterapp/management/commands/generate.py')
        os.system("git commit -m 'first commit to heroku'")
        os.system('git push heroku master')
        os.system('heroku run python manage.py syncdb')
        os.system('heroku run python manage.py migrate')
