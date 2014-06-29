import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-twitter-feed',
    version='0.2',
    packages=['twitter_feed'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to show a Twitter feed.',
    long_description=README,
    url='https://github.com/FrancoisConstant/django-twitter-feed',
    author='Francois Constant',
    author_email='francois.constant@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)