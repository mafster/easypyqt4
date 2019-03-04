from PyQt5 import QtWidgets


class GridWidget(QtWidgets.QWidget):
    """
        Create a Widget with a Grid Layout

    """
    def __init__(self, rows=None, columns=None, fields=[]):
        super(GridWidget, self).__init__()

        if rows:
            self.rows = rows

        if columns:
            self.columns = columns

        self.layout = QtWidgets.QGridLayout()

        self.setLayout(self.layout)

        if fields:
            for each in fields:
                self.add_field(each)

    def get_next_empty_row(self):
        return 1

    def add_field(self, name):
        pass

    def get_column_from_header(self):
        pass

    def add_row_data(self, data):
        """

        :param data:    *(collection)*
        :return:
        """
        row = self.get_next_empty_row()

        for key, value in data.items():

            entry_widget = QtWidgets.QLabel(str(value))
            col = self.get_column_from_header_()

            self.layout.addWidget(entry_widget, row=row, column=col)

            row += 1


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    import collections

    data = collections.OrderedDict()

    data['name'] = 'ball'
    data['project'] = 'test_project'
    data['resource_type'] = 'component'

    fields = ['name', 'project', 'resource_type']
    fw = GridWidget(rows=1, columns=len(fields), fields=fields)

    fw.show()

    fw.add_row_data(data)

    sys.exit(app.exec_())
