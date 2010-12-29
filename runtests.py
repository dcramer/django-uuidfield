#!/usr/bin/env python
import sys
from os.path import dirname, abspath

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='django.db.backends.postgresql_psycopg2',
        DATABASE_NAME='uuidfield_test',
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'uuidfield',
            'uuidfield.tests',
        ],
        ROOT_URLCONF='',
        DEBUG=False,
    )

from django.test.simple import run_tests

def runtests(*test_args):
    if not test_args:
        test_args = ['uuidfield']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive='--no-input' not in sys.argv)
    sys.exit(failures)

if __name__ == '__main__':
    runtests()