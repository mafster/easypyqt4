from PyQt5 import QtCore, QtWidgets
from easypyqt.window import mainwindow

_DOCK_OPTS = QtWidgets.QMainWindow.AnimatedDocks
_DOCK_OPTS |= QtWidgets.QMainWindow.AllowNestedDocks
_DOCK_OPTS |= QtWidgets.QMainWindow.AllowTabbedDocks


class DockingWindow(mainwindow.MainWindow):

    def __init__(self, name='dockingWindow', title=None):
        super(DockingWindow, self).__init__(name=name, title=title)

        self.setWindowFlags(QtCore.Qt.Widget)
        self.setDockOptions(_DOCK_OPTS)
