from datetime import datetime
import sys
import math
from PyQt6 import QtCore, QtGui, QtWidgets

from mainform import Ui_MainWindow
from modbus import ModbusOwen
from orderTableModel import OrderTableModel

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
        
        self.modbus=ModbusOwen()
        self.statusProcess=self.modbus.getStatusProcess()
        
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.controlHeating)
        timer.start(1000)
        
        self.ui.startButton.clicked.connect(self.processStart)
        self.timeStartHeating=datetime.now()
        
        self.getOrders()
        
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
        
        self.plotTime = [0, 1, 2, 4, 5, 6, 9]
        self.plotTemp = [0, 15, 75, 75, 140, 140, 0]
        self.ui.graphHeatingPlot.clear()
        self.ui.graphHeatingPlot.plot(self.plotTime,self.plotTemp)
    
    def processStart(self):
        self.timeStartHeating=datetime.now()
        self.plotPosition=1
        self.modbus.startProcess()
    
    def controlHeating(self):   
        dTime = (datetime.now() - self.timeStartHeating).seconds / 60
        result = self.modbus.getTemp()
        settemp = float(result[1])
        curtemp = float(result[0])
        self.ui.curTempLabel.display(curtemp)
        self.ui.targetTempLabel.display(settemp)
        self.ui.timeWorkLabel.display(math.floor(dTime))
        # Нагрев
        if(self.modbus.getStatusProcess()==2):
            # Включаем охлаждение
            if self.plotPosition == (len(self.plotTime) - 2):
                self.modbus.startCooling()
                return
            curtime = datetime.now()
            if self.plotTime[self.plotPosition] < dTime:
                self.plotPosition+=1
            
            dTemp = (self.plotTemp[self.plotPosition] - self.plotTemp[self.plotPosition - 1]) / (self.plotTime[self.plotPosition] - self.plotTime[self.plotPosition - 1])
            if(dTemp==0):
                dTemp = self.plotTemp[self.plotPosition]
            print(dTemp)
            self.modbus.setTemp(int(dTemp))
         

app = QtWidgets.QApplication([])
application = mainWindow()
application.show()
 
sys.exit(app.exec())