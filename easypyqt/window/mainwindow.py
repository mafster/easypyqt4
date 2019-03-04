from PyQt4 import QtGui, QtCore
from easypyqt.widget import basicwidget


class MainWindow(QtGui.QMainWindow):

    def __init__(self, name=None, title=None, vertical=True, fixedWidth=None, fixedHeight=None):
        """

        :param name:
        :param title:
        :param vertical:
        :param fixedWidth:
        :param fixedHeight:
        """

        super(MainWindow, self).__init__()

        self.title = title

        if name is None:
            name = 'mainWindow'

        self.name = str(name)

        # Set object name and window title
        self.setObjectName(self.name)
        if title:
            self.setWindowTitle(str(title))
        else:
            self.setWindowTitle(self.name)

        self.mainWidget = basicwidget.BasicWidget(vertical=vertical)
        self.setCentralWidget(self.mainWidget)
        self.basic_layout = self.mainWidget.basic_layout  # overrides self.layout builtin method

        # fixed heights
        if fixedWidth:
            self.setFixedWidth(int(fixedWidth))
        if fixedHeight:
            self.setFixedWidth(int(fixedHeight))

        self.setWindowFlags(QtCore.Qt.Window)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    wdg = MainWindow(name='mainWindow')
    wdg.show()

    sys.exit(app.exec_())
