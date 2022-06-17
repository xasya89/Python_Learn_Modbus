import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        if role == Qt.ItemDataRole.ToolTipRole:
            return str(self._data[index.row()][index.column()]) + " tooltip"
        if role == Qt.ItemDataRole.BackgroundRole and index.row() > 2:
            return QtGui.QColor("green")
        
    # def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
    #     if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
    #         return 'Column {}'.format(section + 1)
    #     return super().headerData(section, orientation, role)
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole):
        print(orientation)
        print(role)
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            print(section)
            match section:
                case 0:
                    return "#"
                case 1:
                    return "Дата"
                case 2:
                    return "Заказчик"
                case 3:
                    return "Размер"
            return 'Column- {}'.format(section + 1)
        return super().headerData(section, orientation, role)
    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    
    

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.table.setSortingEnabled(True)
        self.table.selectRow(1)
        self.table.setSelectionBehavior(QtWidgets.QTableView.SelectionBehavior.SelectRows)
        self.table.clicked.connect(self.viewClicked)
        self.setCentralWidget(self.table)
        
    def onStateChanged(self):
        ch = self.sender()
        print(ch.pos())
        ix = self.table.indexAt(ch.pos())
        print(ix.row(), ix.column())
    
    def viewClicked(self, clickedIndex):
        print(clickedIndex.row())
        # row=clickedIndex.row()
        # model=clickedIndex.model()
        #columnsTotal=model.columnCount(None)
        # for i in range(columnsTotal):
        #     self.tableview.selectRow(row)

app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec())