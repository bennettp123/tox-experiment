import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "an_example_project",
    version = "0.0.5",
    author = "Some Guy",
    author_email = "someguy@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "Apache",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_project",
    packages=['an_example_project', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache",
    ],
)
