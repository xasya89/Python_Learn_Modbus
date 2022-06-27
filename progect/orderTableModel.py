from datetime import datetime
import sys
from PyQt6 import QtCore, QtGui, QtWidgets



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