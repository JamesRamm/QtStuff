"""
This module supports both Qt Python API's (PySide and PyQt4)

"""
import os

try:
    from PySide import QtGui, QtCore, QtWebKit
    os.environ['QT_API'] = 'pyside'

    def QtLoadUi(uifile):
        """ Wrapper for loading ui files from PySide """
        from PySide import QtUiTools
        return QtUiTools.QUiLoader().load(uifile)
except ImportError:
    from PyQt4 import QtGui, QtCore, QtWebKit
    os.environ['QT_API'] = 'pyqt'

    import sip
    apiTwo = ['QData', 'QDateTime', 'QString', 'QTextStream',
              'QTime', 'QUrl', 'QVariant']
    for klass in apiTwo:
        sip.setapi(klass, 2)

    QtCore.Signal = QtCore.pyqtSignal
    QtCore.Slot = QtCore.pyqtSlot
    QtCore.QString = str

    def QtLoadUi(uifile):
        """ Wrapper for loading ui files from pyqt """
        from PyQt4 import uic
        return uic.loadUi(uifile)

__all__ = ['QtGui', 'QtCore', 'QtWebKit', 'QtLoadUi']
