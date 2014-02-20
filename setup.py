from setuptools import setup, find_packages

setup(
    name='django-uuidfield',
    version='0.5.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    description='UUIDField in Django',
    url='https://github.com/dcramer/django-uuidfield',
    zip_safe=False,
    install_requires=[
        'django',
    ],
    tests_require=[
        'psycopg2',
        'django-nose',
    ],
    packages=find_packages(),
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
