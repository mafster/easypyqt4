from PyQt4 import QtGui, QtCore


class SearchFieldWidget(QtGui.QLineEdit):

    textEntered = QtCore.pyqtSignal(str)

    def __init__(self, string_list=None):
        super(SearchFieldWidget, self).__init__()

        self.returnPressed.connect(self._selection_made)
        self.setPlaceholderText('search..')

        # Initial
        if string_list:
            self.update_string_list(string_list)

    def _selection_made(self):
        """ Programmatically emit the selection currently made on signal textEntered """
        self.textEntered.emit(str(self.text()))

    def update_string_list(self, string_list):
        """ Recreates the string list """
        model = QtGui.QStringListModel()
        model.setStringList(string_list)

        completer = QtGui.QCompleter()
        completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        completer.setModel(model)
        #completer.setFilterMode(QtCore.Qt.MatchContains) # TODO: Find a replacement for PyQt4
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

        
        self.setCompleter(completer)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    sf = SearchFieldWidget(string_list=['some', 'words', 'in', 'my', 'dictionary'])
    sf.show()

    sys.exit(app.exec_())
