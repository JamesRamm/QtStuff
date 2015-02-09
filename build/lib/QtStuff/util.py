""" Utility functions for using Qt """
from QtStuff.QtVariant import QtCore
import weakref
import os
import logging

class QCacheManager(type(QtCore.QObject)):
    """
    Metaclass to enabling caching of PySide objects.
    """
    def __init__(self, *args, **kwargs):
        super(QCacheManager, self).__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super(QCacheManager, self).__call__(*args)
            self.__cache[args] = obj
            return obj

class QLogHandler(QtCore.QObject):
    """
    A file-like object to use in a StreamHandler for python logging
    Will accept the logging message and emit it as a PySide/PyQt signal

    Example
    -------
    ::

        import logging
        import sys
        from QtStuff import QtGui
        from QtStuff.util import QLogHandler

        class MainWindow(QtGui.QMainWindow):
            def __init__(self, parent=None):
                super(MainWindow, self).__init__(parent)
                self.statusbar = self.statusBar()
                debug_log.stream.logged.connect(self.statusbar.showMessage)

                logger.debug("This is a test message")

        if __name__ == '__main__':             
            logging.basicConfig(level = logging.DEBUG)

            debug_log = logging.StreamHandler(stream = QLogHandler())
            debug_log.setLevel(logging.DEBUG)

            logger = logging.getLogger(__name__)
            logger.addHandler(debug_log)
            main = MainWindow()
            main.show()
            sys.exit(app.exec_())
    """
    logged = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(QLogHandler, self).__init__(parent)

    def write(self, record):
        self.logged.emit(record)

def workInThread(workerClass, workerFunc, finishedFunc=None):
    """
    Carry out processing in a seperate thread.
    The worker object must define a 'finished' signal which should
    be emitted when the work is finished. This will inform the
    thread to quit.
    :parent: the object which will act as a 'parent' to the thread.
    Must be an object which will persist for the duration of the
    work (e.g. a widget or similar) otherwise the thread may quit (?)
    :workerClass: the object which will do the work and requires
    moving to the thread. **Must** be a child of QObject.

    :workerFunc:  the function (i.e. workerClass.func) to be
    called when the thread starts

    :finishedFunc: the function to be called when the thread
    is finished.
    """
    workerThread = QtCore.QThread()
    #Moves the worker to the thread so that it will be executed there...
    workerClass.moveToThread(workerThread)

     # When the worker is finished, close the thread
    workerClass.finished.connect(workerThread.exit)
    # Connect signals and slots
    # This function should carry out the processing.
    workerThread.started.connect(workerFunc)
     # If finishedFunc is defined, call it when the thread exits.
     # This function would usually do things such as inform the
     # user the operation has finished/close a progress bar etc...
    if finishedFunc:
        workerThread.finished.connect(finishedFunc)
    workerThread.start()
    return workerThread
