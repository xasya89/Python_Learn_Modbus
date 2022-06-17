from datetime import datetime
import sys
from PyQt6 import QtCore, QtGui, QtWidgets

from mainform import Ui_MainWindow

class OrderTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(OrderTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%d.%m.%Y")
            return value
        
        if role == QtCore.Qt.ItemDataRole.ToolTipRole:
            return str(self._data[index.row()][index.column()]) + " tooltip"
        if role == QtCore.Qt.ItemDataRole.BackgroundRole and index.row() > 2:
            return QtGui.QColor("green")
        
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.ItemDataRole.DisplayRole):
        if orientation == QtCore.Qt.Orientation.Horizontal and role == QtCore.Qt.ItemDataRole.DisplayRole:
            match section:
                case 0:
                    return "Заказ"
                case 1:
                    return "Дата"
                case 2:
                    return "Заказчик"
            return 'Columning {}'.format(section + 1)
        return super().headerData(section, orientation, role)
    
    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class MyHeaderView(QtWidgets.QHeaderView):
    def __init__(self,parent):
        QtWidgets.QHeaderView.__init__(self,QtCore.Qt.Orientation.Horizontal,parent)
        self.sectionResized.connect(self.myresize)

    def myresize(self, *args):
        ws=[]
        for c in range(self.count()):
            wii=self.sectionSize(c)
            ws.append(wii)

        if args[0]>0 or args[0]<self.count():
            for ii in range(args[0],self.count()):
                if ii==args[0]:
                    # resize present column
                    self.resizeSection(ii,args[2])
                elif ii==args[0]+1:
                    # if present column expands, shrink the one to the right
                    self.resizeSection(ii,ws[ii]-(args[2]-args[1]))
                else:
                    # keep all others as they were
                    self.resizeSection(ii,ws[ii])

    def resizeEvent(self, event):
        super(QtWidgets.QHeaderView, self).resizeEvent(event)
        self.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeMode.Stretch)
        for column in range(self.count()):
            self.setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeMode.Stretch)
            width = self.sectionSize(column)
            self.setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeMode.Interactive)
            self.resizeSection(column, width)
        return
    
class mainWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.getOrders()
        self.ui.curTempLabel.value
        
    def getOrders(self):
        data = [
          [4, datetime(2022, 6,21), "ООО Мир стекол"],
          [1, datetime(2022, 6,21), "ООО Мир стекол"],
          [3, datetime(2022, 6,21), "ООО Мир стекол"],
          [3, datetime(2022, 6,21), "ООО Мир стекол"],
          [7, datetime(2022, 6,21), "ООО Мир стекол"],
        ]
        self.model = OrderTableModel(data)
        hh=MyHeaderView(self)
        self.ui.ordersTable.setHorizontalHeader(hh)
        self.ui.ordersTable.setModel(self.model)
        self.ui.ordersTable.setSortingEnabled(True)
        self.ui.ordersTable.selectRow(1)
        self.ui.ordersTable.setSelectionBehavior(QtWidgets.QTableView.SelectionBehavior.SelectRows)
        self.ui.ordersTable.clicked.connect(self.orderChange)
    
    def orderChange(self, clickedIndex):
        print(clickedIndex.row())
        
        x = [0, 15, 20, 45, 55, 110, 130]
        y = [0, 15, 75, 75, 140, 140, 0]
        self.ui.graphHeatingPlot.clear()
        self.ui.graphHeatingPlot.plot(x,y)

app = QtWidgets.QApplication([])
application = mainWindow()
application.show()
 
sys.exit(app.exec())