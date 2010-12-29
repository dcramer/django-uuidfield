#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test

class mytest(test):
    def run(self, *args, **kwargs):
        from runtests import runtests
        runtests()

setup(
    name='django-uuidfield',
    version='0.2',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    description='UUIDField in Django',
    url='https://github.com/dcramer/django-uuidfield',
    zip_safe=False,
    install_requires=[
        'uuid',
    ],
    packages=find_packages(),
    test_suite = 'uuidfield.tests',
    include_package_data=True,
    cmdclass={"test": mytest},
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)