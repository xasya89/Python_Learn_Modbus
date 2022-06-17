from random import random
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import pyqtgraph as pg
import random


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn1.clicked.connect(self.btnClick)
        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.ui.tableOrders.setColumnCount(3)
        self.ui.tableOrders.setHorizontalHeaderLabels("Заказ", "Дата", "Заказчик")
        self.ui.tableOrders.setItem(0,1,QTableWidgetItem("007"))
        
    
    def btnClick(self):
        self.ui.inp1.setText("hello")
        x = []
        y = []
        x.append(random.randint(1,10))
        y.append(random.randint(1,10))
        x.append(random.randint(1,10))
        y.append(random.randint(1,10))
        x.append(random.randint(1,10))
        y.append(random.randint(1,10))
        self.ui.widget1.clear()
        pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.PenStyle.DashLine)
        self.ui.widget1.plot(x,y,pen=pen)
 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())