from PyQt4 import QtGui

from easypyqt.widget import buttongroupwidget
from easypyqt.dialog import basicdialog

_DEFAULT_BUTTON_LIST = [
    ('yes', 'Yes'),
    ('no', 'No'),
    ('cancel', 'Cancel'),
]

# TODO: Handle custom button list


class ConfirmDialog(basicdialog.BasicDialog):

    def __init__(self, title=None, message=None, vertical=True, auto_exec=False):
        super(ConfirmDialog, self).__init__(title=title, vertical=vertical, auto_exec=False)

        self.title = title or 'Confirm...'
        self.message = message or '..'

        # Widgets
        self.messageLabel = QtGui.QLabel(self.message)
        self.button_group = buttongroupwidget.ButtonGroupWidget(button_list=_DEFAULT_BUTTON_LIST)

        # Layout
        self.basic_layout.addWidget(self.messageLabel)
        self.basic_layout.addWidget(self.button_group)

        # Signals
        self.button_group.yes.clicked.connect(self.accept)
        self.button_group.no.clicked.connect(self.reject)
        self.button_group.cancel.clicked.connect(self.cancel_)

        self.setWindowTitle(self.title)

        if auto_exec:
            self.exec_()

    def cancel_(self):
        """

        :return:
        """
        self.result_ = 'cancel'
        self.reject()


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    pd = ConfirmDialog(title='Confirm something', message='are you sure?', vertical=True)

    pd.exec_()

    sys.exit(app.exec_())
