#!/usr/bin/env python

"""
Playing around with QMainWindow's nested within each other
as dock widgets.
"""

from random import randint

from PyQt5 import QtCore, QtWidgets


_DOCK_OPTS = QtWidgets.QMainWindow.AnimatedDocks
_DOCK_OPTS |= QtWidgets.QMainWindow.AllowNestedDocks
_DOCK_OPTS |= QtWidgets.QMainWindow.AllowTabbedDocks

_DOCK_COUNT = 0
_DOCK_POSITIONS = (
    QtCore.Qt.LeftDockWidgetArea,
    QtCore.Qt.TopDockWidgetArea,
    QtCore.Qt.RightDockWidgetArea,
    QtCore.Qt.BottomDockWidgetArea
)


def main():

    mainWindow = QtWidgets.QMainWindow()
    mainWindow.resize(1024,768)
    mainWindow.setDockOptions(_DOCK_OPTS)

    widget = QtWidgets.QLabel("MAIN APP CONTENT AREA")
    widget.setMinimumSize(300,200)
    widget.setFrameStyle(widget.Box)
    mainWindow.setCentralWidget(widget)
    mainWindow.centralWidget().hide()
    addDocks(mainWindow, "Main Dock")

    mainWindow.show()
    mainWindow.raise_()

    return mainWindow


def addDocks(window, name):
    global _DOCK_COUNT

    for pos in _DOCK_POSITIONS:

        for _ in range(2):
            _DOCK_COUNT += 1

            sub = QtWidgets.QMainWindow()
            sub.setWindowFlags(QtCore.Qt.Widget)
            sub.setDockOptions(_DOCK_OPTS)

            color = tuple(randint(20, 230) for _ in range(3))

            label = QtWidgets.QLabel("%s %d content area" % (name, _DOCK_COUNT), sub)
            label.setMinimumHeight(25)
            label.setStyleSheet("background-color: rgb(%d, %d, %d)" % color)
            sub.setCentralWidget(label)

            dock = QtWidgets.QDockWidget("%s %d title bar" % (name, _DOCK_COUNT))
            dock.setWidget(sub)

            window.addDockWidget(pos, dock)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mainWindow = main()

app.exec_()
