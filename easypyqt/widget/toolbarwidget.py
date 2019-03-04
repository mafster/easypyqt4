import os

from PyQt5 import QtGui, QtWidgets


class ToolBarWidget(QtWidgets.QToolBar):

    def __init__(self, *args):
        super(ToolBarWidget, self).__init__(*args)

    def add_action_tool_button(self, name, icon_path=None):
        """
        Add an action to the toolbar with a nice name and icon. Sets the objectName of the action to the name passed
        :param name:        *(str)* name of the action
        :param icon_path:   *(str)* absolute filepath to icon
        :return:            *(QAction)* returns the action created
        """
        if icon_path and os.path.isfile(icon_path):
            action = QtWidgets.QAction(QtGui.QIcon(icon_path), '&{}'.format(name.title()), self)
        else:
            action = QtWidgets.QAction('&{}'.format(name.title()), self)

        action.setObjectName(name)
        self.addAction(action)

        return action
