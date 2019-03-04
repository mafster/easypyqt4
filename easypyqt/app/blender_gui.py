# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Qt Integration",
    "author": "Vincent Gires",
    "description": "Qt Integration Example",
    "version": (0, 0, 1),
    "blender": (2, 7, 8),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Qt"}

import bpy
import logging

from PyQt5 import QtWidgets, QtCore


class EXAMPLE_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.widget_close = None
        self.context = None
        self.initUI()

    def initUI(self):
        self.resize(720, 300)
        self.setWindowTitle("QT Window")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        label = QtWidgets.QLabel('Label')
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label)
        self.setLayout(layout)

        self.show()

    def closeEvent(self, event):
        self.widget_close = True
        self.deleteLater()


class QT_WINDOW_EventLoopOp(bpy.types.Operator):

    bl_idname = "qt_window.event_loop"
    bl_label = "PyQt Event Loop"

    _timer = None

    def modal(self, context, event):
        wm = context.window_manager
        if self.widget.widget_close:
            logging.debug('cancel modal operator')
            wm.event_timer_remove(self._timer)
            return {"CANCELLED"}
        else:
            logging.debug('process the events for Qt window')
            self.event_loop.processEvents()
            self.app.sendPostedEvents(None, 0)

        return {'PASS_THROUGH'}

    def execute(self, context):
        logging.debug('execute operator')

        self.app = QtWidgets.QApplication.instance()
        # instance() gives the possibility to have multiple windows and close it one by one
        if not self.app:
            self.app = QtWidgets.QApplication(['blender'])
        self.event_loop = QtCore.QEventLoop()

        self.widget = EXAMPLE_Widget()
        #self.widget = QtWidgets.QWidget()
        #self.widget.setFixedSize(200,100)
        #self.widget.show()

        self.widget.context = context

        logging.debug(self.app)
        logging.debug(self.widget)

        # run modal
        wm = context.window_manager
        self._timer = wm.event_timer_add(1 / 120, context.window)
        context.window_manager.modal_handler_add(self)

        return {'RUNNING_MODAL'}


def register():
    bpy.utils.register_class(QT_WINDOW_EventLoopOp)


def unregister():
    bpy.utils.unregister_class(QT_WINDOW_EventLoopOp)


if __name__ == "__main__":
    register()

