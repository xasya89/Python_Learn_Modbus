# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ordersTable = QtWidgets.QTableView(self.centralwidget)
        self.ordersTable.setGeometry(QtCore.QRect(0, 411, 821, 301))
        self.ordersTable.setObjectName("ordersTable")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(860, 430, 111, 71))
        self.startButton.setObjectName("startButton")
        pg.setConfigOption('background', 'white')
        pg.setConfigOption('foreground', 'blue')
        # self.graphHeatingPlot = QtWidgets.QWidget(self.centralwidget)
        self.graphHeatingPlot = pg.PlotWidget(self.centralwidget)
        self.graphHeatingPlot.setGeometry(QtCore.QRect(0, 0, 771, 291))
        self.graphHeatingPlot.setObjectName("graphHeatingPlot")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 0, 161, 21))
        self.label.setObjectName("label")
        self.curTempLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.curTempLabel.setGeometry(QtCore.QRect(780, 20, 171, 51))
        self.curTempLabel.setObjectName("curTempLabel")
        self.targetTempLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.targetTempLabel.setGeometry(QtCore.QRect(780, 100, 171, 51))
        self.targetTempLabel.setObjectName("targetTempLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(780, 80, 211, 21))
        self.label_2.setObjectName("label_2")
        self.timeWorkLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.timeWorkLabel.setGeometry(QtCore.QRect(780, 190, 171, 51))
        self.timeWorkLabel.setObjectName("timeWorkLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(780, 170, 161, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(960, 210, 47, 13))
        self.label_4.setObjectName("label_4")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(870, 570, 111, 71))
        self.stopButton.setObjectName("stopButton")
        self.messageTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.messageTextEdit.setGeometry(QtCore.QRect(10, 320, 761, 71))
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 390, 91, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "??????????"))
        self.label.setText(_translate("MainWindow", "?????????????????????? ????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????? ??????????????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????? ????????????"))
        self.label_4.setText(_translate("MainWindow", "??????"))
        self.stopButton.setText(_translate("MainWindow", "????????"))
        self.label_5.setText(_translate("MainWindow", "??????????????????"))
        self.label_6.setText(_translate("MainWindow", "????????????"))
