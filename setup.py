from distutils.core import setup
from setuptools import find_packages

setup(
    name='db_connector',
    version='1.0',
    author=u'Brandon Chinn',
    author_email='brandonchinn178@gmail.com',
    packages=find_packages(),
    url='http://github.com/brandonchinn178/db_connector',
    description='Defines a class for connecting to a MySQL databases',
    long_description=open('README.txt').read(),
    zip_safe=False,
)