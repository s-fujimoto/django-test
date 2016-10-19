#!/usr/bin/env python

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


# Hack to prevent "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when setup.py exits
# (see http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass


install_requires = [
    "Django>=1.8.1,<1.11",
    "djangorestframework>=3.1.3",
    "Pillow>=2.6.1",
]

# Testing dependencies
testing_extras = [
    # Required for running the tests
    'mock>=1.0.0',
    'python-dateutil>=2.2',
    'pytz>=2014.7',
    'Pillow>=2.7.0',
    'Jinja2>=2.8,<3.0',
    'boto3>=1.1,<1.2',

    # For coverage and PEP8 linting
    'coverage>=3.7.0',
    'flake8>=2.2.0',
    'isort>=4.2.0',
]

setup(
    name='django-test',
    version='0.0.1',
    description='A Django content management system focused on flexibility and user experience',
    author='Shinji Fujimoto',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    zip_safe=False,
)