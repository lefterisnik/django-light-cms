import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-loose-cms',
    version='0.2.1',
    packages=['loosecms'],
    include_package_data=True,
    license='BSD License',
    description='Open source CMS based on the django framework.',
    long_description=README,
    author='Lefteris Nikoltsios',
    author_email='lefteris.nikoltsios@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.8,<1.9',
        'django-ckeditor',
        'tinycss',
        'beautifulsoup4',
        'bootstrap-admin',
    ],
)
