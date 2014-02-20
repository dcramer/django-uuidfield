#!/usr/bin/env python
import sys
from django.conf import settings
from optparse import OptionParser

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='django.db.backends.sqlite3',
        DATABASE_NAME='uuidfield_test',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'uuidfield_test',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'uuidfield',
            'uuidfield.tests',
        ],
        ROOT_URLCONF='',
        DEBUG=False,
    )

from django_nose import NoseTestSuiteRunner


from runtests import runtests

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store', default=1, type=int)
    parser.add_options(NoseTestSuiteRunner.options)
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)
