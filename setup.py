#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Subset_Component",
    version="0.0.1",
    author="Inaki Madinabeitia",
    description="Subset Component",
    license="GNU",
    keywords="",
    packages=['src', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
    ],
)
