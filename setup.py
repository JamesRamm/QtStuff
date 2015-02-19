#!/usr/bin/env python
from distutils.core import setup

""" Setup script for QtStuff """

setup(name = "QtStuff",
      version = "0.4",
      description="Compatibility layer and helper classes for PySide/PyQt4/PyQt5",
      author = 'James Ramm',
      author_email = 'james.ramm@jbarisk.com',
      packages = ['QtStuff'],
      package_data = {'QtStuff': ['Images/*.*', 'Images/GreyCircles/*.*', 'Images/OrangeIcons/*.*']})