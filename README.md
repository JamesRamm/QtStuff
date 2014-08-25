QtStuff
=======
[![Documentation Status](https://readthedocs.org/projects/qtstuff/badge/?version=latest)](https://readthedocs.org/projects/qtstuff/?badge=latest)

QtStuff: Classes and helper functions for working with PySide/PyQt

QtStuff ('Cute Stuff') provides helpful classes and a nice icon set for use with PySide/PyQt. It also provides a PySide/PyQt agnostic wrapper around the library. No matter which version you have installed, just do:

    from QtStuff import QtCore, QtGui, QtWebKit, QtLoadUi

Most functions and classes in the library we're found in the various Qt Website, forums, stackOverflow etc..


Features
----------

Some of the features of QtStuff include:

- A compatibility layer to allow your application to support PyQt or PySide 
- A large icon set with corresponding API to easily get hold of `QIcon`objects for each item image.
- Utility functions for logging, caching `QObject`derived classes, easy threading...
- Mixins for creating popup dialogs
- A wonderful colorpicker by Victor Wahlstrom
- A simple interactive console widget 
