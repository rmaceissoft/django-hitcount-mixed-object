import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-hitcount-mixed-object",
    version = "0.1",
    description = "holds hit count of mixed objects represented at relation model using NoSQL db",
    long_description = read('README.rst'),
    url = 'https://github.com/rmaceissoft/django-hitcount-mixed-object',
    author = 'Reiner Marquez',
    author_email = 'rmaceissoft@gmail.com',
    packages = find_packages(exclude=['tests', 'example', 'docs']),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)