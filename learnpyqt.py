from random import random
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import pyqtgraph as pg
import random
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn1.clicked.connect(self.btnClick)
        
    
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