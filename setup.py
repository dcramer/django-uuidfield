#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-uuidfield',
    version=".".join(map(str, __import__('uuidfield').__version__)),
    author='David Cramer',
    author_email='dcramer@gmail.com',
    description='UUIDField in Django',
    url='http://github.com/dcramer/django-uuidfield',
    zip_safe=False,
    install_requires=[
        'uuid',
    ]
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)