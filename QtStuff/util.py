""" Utility functions for using Qt """
from QtStuff.QtVariant import QtCore
import weakref
import os

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


class Logger(QtCore.QObject):
    """
    Logs all messages and emits a signal for each level of severity.
    Enables errors etc to be accessed from anywhere and handle in any
    number of ways (that does not involve horrible popup dialogs)
    """
    __metaclass__ = QCacheManager
    # Signal to be used by the logger
    info = QtCore.Signal(str)
    warn = QtCore.Signal(str)
    error = QtCore.Signal(str)
    priority = QtCore.Signal(str)
    def __init__(self, name='applicationLog', path=""):
        super(Logger, self).__init__()
        self.name = name
        self.path = path

    def log(self, message, severity, toFile=True):
        """
        Message handler. Emits messages, where severity indicates
        the signal to use. Will also write the message out to a log
        file.
        """
        fname = "".join([self.name, ".log"])
        fname = os.path.join(self.path, self.name)
        severity = severity.lower()
        signal = getattr(self, severity)
        signal.emit(message)

        if toFile:
            f = open(fname, 'a+')
            f.write("{0}: {1}\n".format(severity, message))
            f.close()

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
