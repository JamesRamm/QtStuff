#!/usr/bin/env python
from distutils.core import setup

""" Setup script for QtStuff """

setup(name = "QtStuff",
      version = "0.1",
      author = 'James Ramm',
      author_email = 'james.ramm@jbarisk.com',
      packages = ['QtStuff'],
      package_data = ['Images/*.*', 'Images/GreyCircles/*.*', 'Images/OrangeIcons/*.*'])