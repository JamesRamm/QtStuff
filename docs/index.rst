.. _QtStuff


QtStuff
==========

QtStuff is a python package for working with the PySide/PyQt packages. 
It aims to be a toolkit for making it easy to develop high quality GUI's. 

There are various recipes for PySide and PyQt kicking around the web, with many that
are extremely useful (or just cool). Unfortunately, there is no one resource to gather
and formalise these tidbits of code. 
QtStuff aims to fill that gap. 


Features
---------

* A PySide/PyQt compatibility layer (just type `from QtStuff import QtGui, QtCore`)
* A nice, ready-to-use icon set
* Widgets: colorpicker, interactive console, an 'easy' main window...
* Utility functions: a logger, an object cache (so you don't have to pass around references to QObjects between widgets), a 'thread-helper'
* Mixins: Popup-dialogs, frameless windows...


Installation
---------------

Download QtStuff and unzip to a folder of your choice. Then run::

    python setup.py install
    



Contribute
-------------

Source Code: https://github.com/JamesRamm/QtStuff
Issue Tracker: https://github.com/JamesRamm/QtStuff/issues


License
---------
QtStuff is licensed under the GPL v2 license
