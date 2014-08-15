from QtVariant import QtCore, QtGui

class PopupDialogMixin(object):
    """
    Mixin for making a QDialog a 'popup' dialog.
    I.e: No frame, appears directly under the calling widget and dissapears when the user clicks elsewhere
    """
    __slots__ = ()
    def makePopup(self, callWidget):
        self.setContentsMargins(0,0,0,0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
        self.setObjectName('PopupDialog') # Necessary?

        point = callWidget.rect().bottomRight()
        global_point = callWidget.mapToGlobal(point)
        self.move(global_point - QtCore.QPoint(self.width()/2, 0))      

    def resizeEvent(self, event):
        """ Overriding resizeEvent to force rounded corners """
        leBitmap = QtGui.QBitmap(self.size())
        painter = QtGui.QPainter(leBitmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtCore.Qt.color1)
        painter.drawRoundedRect(self.rect(), 5, 5)
        painter.end()

        self.setMask(leBitmap)