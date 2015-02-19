import sys
import imp
binding_order = getattr(sys, 'QT_BINDING_ORDER', ['PySide', 'PyQt5', 'PyQt4'])
for binding_name in binding_order:
    try:
        mod = imp.load_module(binding_name, *imp.find_module(binding_name))
        break
    except ImportError:
        continue 
        
if binding_name == "PySide":    
    from PySide import QtCore, QtGui, QtWebKit, QtSvg, QtSql, QtXml, QtOpenGL, QtNetwork, QtTest, QtScript
elif binding_name == "PyQt4":    
    import sip
    try:
        sip.setapi('QDate', 2)
        sip.setapi('QDateTime', 2)
        sip.setapi('QString', 2)
        sip.setapi('QTextStream', 2)
        sip.setapi('QTime', 2)
        sip.setapi('QUrl', 2)
        sip.setapi('QVariant', 2)
    except ValueError as e:
        raise RuntimeError('Could not set API version (%s): did you import PyQt4 directly?' % e)
    from PyQt4 import QtCore, QtGui, QtWebKit, QtSvg, QtSql, QtXml, QtOpenGL, QtNetwork, QtTest, QtScript

    # set some names for compatibility with PySide
    sys.modules['QtCore'].Signal = sys.modules['QtCore'].pyqtSignal
    sys.modules['QtCore'].Slot = sys.modules['QtCore'].pyqtSlot
    sys.modules['QtCore'].Property = sys.modules['QtCore'].pyqtProperty
    
elif binding_name == "PyQt5":    
    from PyQt5 import QtCore, QtGui, QtWebKit, QtSvg, QtSql, QtXml, QtOpenGL, QtNetwork, QtTest, QtScript, QtWidgets, QtWebKitWidgets, QtPrintSupport

import gui
import console
import mixins
import colorpicker
import util
