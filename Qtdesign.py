# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V0.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from mplcanvaswrapper import MplCanvasWrapper



class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1229, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 50, 750, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.position = MplCanvasWrapper(parent=self.centralwidget,title="position",valueName='mm')
        self.position.setGeometry(QtCore.QRect(40, 150, 361, 191))
        self.position.setObjectName("position")
        self.force = MplCanvasWrapper(parent=self.centralwidget,title="force",valueName="N")
        self.force.setGeometry(QtCore.QRect(430, 150, 361, 191))
        self.force.setObjectName("force")
        self.speed = MplCanvasWrapper(parent=self.centralwidget,title='speed',valueName='m/s')
        self.speed.setGeometry(QtCore.QRect(820, 150, 361, 191))
        self.speed.setObjectName("speed")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 400, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 400, 301, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1030, 400, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 480, 711, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../project/image.PNG"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(950, 120, 51, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(1000, 120, 121, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.Time.setFont(font)
        self.Time.setText("")
        self.Time.setObjectName("Time")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1229, 23))
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
        self.label.setText(_translate("MainWindow", "Intelligent parameter detection system"))
        self.label_2.setText(_translate("MainWindow", "State Analysis"))
        self.label_5.setText(_translate("MainWindow", "None"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.label_4.setText(_translate("MainWindow", "Time"))