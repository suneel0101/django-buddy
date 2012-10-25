#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

from django.core.management.commands.runserver import Command as BaseCommand


def run_external_command(command, environment_variable, msg):
    out = open('/dev/null', 'w')

    try:
        if not os.getenv(environment_variable, False):
            p = subprocess.Popen(command.split(), stderr=out, stdout=out)
            os.environ[environment_variable] = 'Running'
            return p
    except OSError, e:
        print u"oops {} {}".format(unicode(e), unicode(msg))
        os.environ[environment_variable] = 'Failed'


class Command(BaseCommand):
    processes = []

    def run_dependencies(self):
        self.processes.append(
            run_external_command(
                command='compass watch media/',
                environment_variable='YIPIT_COMPASSD',
                msg=(u"\033[1;33mCompass is not installed. Install it with "
                "`gem install compass -n /usr/local/bin`.\033[0m")))

    def kill_processes(self):
        for p in self.processes:
            if p:
                p.kill()

    def handle(self, *args, **options):
        self.run_dependencies()
        try:
            super(Command, self).handle(*args, **options)
        except:
            self.kill_processes()
            raise
