import sys
import images
import os
from QtStuff import QtCore, QtGui

class JWindow(QtGui.QMainWindow):
    def __init__(self, name, iconName = "risk_logo"):
        """
        Provides a basic application window with the following already initialised:
        - Status bar (JWindow.statusbar)
        - Exit action (JWindow.exitAction).
        - Centered on screen
        - Window title
        - Central Widget (JWindow.mainWidget). This is a QFrame instance.
        - closeEvent, which intercepts 'close' commands and displays an 'Are you sure?' dialog.

        Usage:
        Inherit from JWindow and redefine the initUI method.
        """
        super(JWindow, self).__init__()
        self.standard_setup(name, iconName)  
        self.standard_actions()
        self.initUI()

    def initUI(self):
        raise NotImplementedError("Override this method to add functionality to your GUI")

    def standard_setup(self, name, iconName = "risk_logo"):
        """ Setups a main window with a central widget, name, statusbar, JBA logo and centers on the screen"""
        self.mainWidget = QtGui.QFrame()
        self.mainWidget.setObjectName("mainWidget")
        self.setCentralWidget(self.mainWidget)
        self.statusbar = self.statusBar()
        self.mainWidget.setContentsMargins(0,0,0,0)
        self.setWindowTitle(name)
        self.setWindowIcon(icons(iconName))
        self.resize(1046, 600) #width, height.
        self.center()   

    def standard_actions(self):
        self.exitAction = QtGui.QAction(icons('exit'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(QtCore.QCoreApplication.instance().exit)    

    def make_frameless(self):
        """ 
        Makes a 'frameless' window, but maintains title bar, resize and dragndrop
        TODO: Implement this as a mixin
        """
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def center(self):
        """ Centres the window on the screen """
        qr = self.frameGeometry() # rect specifying geometry of self
        cp = QtGui.QDesktopWidget().availableGeometry().center() # Gets the screen resolution and then the centre point
        qr.moveCenter(cp) # Move the center of the rectangle to the centre of the screen
        self.move(qr.topLeft()) # move top left point of app window to top left of  rectangle

    def closeEvent(self, event = QtGui.QCloseEvent(QtCore.QEvent.Close)):
        """ Intercepts close events and asks if the user really wants to quit """
        msgBox = ExitMessage()

        msgBox.run()

        if msgBox.clickedButton() == msgBox.acceptB:
            event.accept()
        else:
            event.ignore()

class ExitMessage(QtGui.QMessageBox):
    
    def __init___(self, parent = None):
        """ A simple dialog for asking for confirmation """
        super(ExitMessage, self).__init__(parent)

    def run(self, text = "Quit?"):
        self.setText(text)
        self.setIconPixmap(QtGui.QPixmap(':Images/GreyCircles/question.png'))
        self.setWindowIcon(icons('risk_logo'))
        self.setWindowTitle("Quit")
        self.acceptB = self.addButton(self.tr("Yes"), QtGui.QMessageBox.ActionRole)
        self.acceptB.setIcon(icons('check'))
        self.acceptB.setText("")
        self.acceptB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
        self.cancelB = self.addButton(self.tr("No"), QtGui.QMessageBox.ActionRole)
        self.cancelB.setIcon(icons('cross'))
        self.cancelB.setText("")
        self.cancelB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 

        self.exec_()

class AppError(QtGui.QErrorMessage):
    """ Displays an error message to the user. TODO: Get rid of 'python' as window title. Customise appearance """
    def __init__(self, message, parent = None):

        super(AppError, self).__init__(parent)
        self.showMessage(message)
        self.setWindowTitle('Application Error')

def icons(name):
    """ Returns a QtGui.QIcon for the given icon name """
    val = _iconFiles[name]
    ico = QtGui.QIcon()
    ico.addFile(val[0], mode = QtGui.QIcon.Mode.Normal)
    ico.addFile(val[1], mode = QtGui.QIcon.Mode.Active)

    return ico
    
def what_icons():
    """ Returns the names of available icons """
    return _iconFiles.keys()

_iconFiles = {'more':[':Images/GreyCircles/more.png',':Images/GreyCircles/more_halo.png'],
              'annotate': [':Images/GreyCircles/annotate.png',':Images/GreyCircles/annotate_halo_w.png'],
              'book': [':Images/GreyCircles/book.png',':Images/GreyCircles/book_halo_w.png'],
              'check': [':Images/GreyCircles/check.png',':Images/GreyCircles/check_halo_w.png'],
              'cog': [':Images/GreyCircles/cog.png',':Images/GreyCircles/cog_halo_w.png'],
              'cross': [':Images/GreyCircles/cross.png',':Images/GreyCircles/cross_halo_w.png'],
              'excel': [':Images/GreyCircles/excel.png',':Images/GreyCircles/excel_halo_W.png'],
              'exit': [':Images/GreyCircles/exit.png',':Images/GreyCircles/exit_halo_w.png'],
              'filter': [':Images/GreyCircles/filter.png',':Images/GreyCircles/filter.png'],
              'filter_empty': [':Images/GreyCircles/filter_empty.png',':Images/GreyCircles/filter_empty_halo_w.png'],
              'help': [':Images/GreyCircles/help.png',':Images/GreyCircles/help_halo_w.png'],
              'open': [':Images/GreyCircles/open.png',':Images/GreyCircles/open_halo_w.png'],
              'python': [':Images/GreyCircles/python.png',':Images/GreyCircles/python_halo_w.png'],
              'question': [':Images/GreyCircles/question.png',':Images/GreyCircles/question_halo_w.png'],
              'recycle': [':Images/GreyCircles/recycle.png',':Images/GreyCircles/recycle_halo_w.png'],
              'save': [':Images/GreyCircles/save.png',':Images/GreyCircles/save_halo_w.png'],
              'table': [':Images/GreyCircles/table.png',':Images/GreyCircles/table_halo_w.png'],
              'info':  [':Images/GreyCircles/info.png',':Images/GreyCircles/info_halo_w.png'],
              'polygon': [':Images/Misc/polygon.png',':Images/Misc/polygon.png'],
              'line': [':Images/Misc/line.png',':Images/Misc/line.png'],
              'update': [':Images/GreyCircles/update.png',':Images/GreyCircles/update_halo_w.png'],
              'setupDB': [':Images/GreyCircles/setupDB.png',':Images/GreyCircles/setupDB_halo_w.png'],
              'emptyDB': [':Images/GreyCircles/emptyDB.png',':Images/GreyCircles/emptyDB_halo_w.png'],
              'polygon_circle': [':Images/GreyCircles/polygon_circle.png',':Images/GreyCircles/polygon_circle.png'],
              'create_plot': [':Images/OrangeIcons/create_plot.png',':Images/OrangeIcons/create_plot.png'],
              'plot_wizard': [':Images/OrangeIcons/plot_wizard.png',':Images/OrangeIcons/plot_wizard.png'],
              'remove_plot': [':Images/OrangeIcons/remove_plot.png',':Images/OrangeIcons/remove_plot.png'],
              'reset_chart': [':Images/OrangeIcons/reset_chart.png',':Images/OrangeIcons/reset_chart.png'],
              'table_add': [':Images/OrangeIcons/table_add.png',':Images/OrangeIcons/table_add.png'],
              'table_bin': [':Images/OrangeIcons/table_bin.png',':Images/OrangeIcons/table_bin.png'],
              'table_delete': [':Images/OrangeIcons/table_delete.png',':Images/OrangeIcons/table_delete.png'],
              'solid_line': [':Images/Misc/solidLine.bmp',':Images/Misc/solidLine.bmp'],
              'dashed_line': [':Images/Misc/dashedLine.bmp',':Images/Misc/dashedLine.bmp'],
              'dotted_line': [':Images/Misc/dottedLine.bmp',':Images/Misc/dottedLine.bmp'],
              'dash_dot_line': [':Images/Misc/dashDotLine.bmp',':Images/Misc/dashDotLine.bmp'],
              'black': [':Images/Misc/black.png',':Images/Misc/black.png'],
              'light_blue': [':Images/Misc/light_blue.png',':Images/Misc/light_blue.png'],
              'risk_logo': [':Images/TransLogo.png',':Images/TransLogo.png'],
              'dropdown': [':Images/Misc/dropdown.png',':Images/Misc/dropdown.png']}

