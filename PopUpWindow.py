# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainDataWidget = PlotWidget(self.centralwidget)
        self.MainDataWidget.setObjectName("MainDataWidget")
        self.verticalLayout_2.addWidget(self.MainDataWidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SavedData1Widget = PlotWidget(self.centralwidget)
        self.SavedData1Widget.setObjectName("SavedData1Widget")
        self.verticalLayout_3.addWidget(self.SavedData1Widget)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LoadFiletoWidget1Button = QtWidgets.QPushButton(self.centralwidget)
        self.LoadFiletoWidget1Button.setObjectName("LoadFiletoWidget1Button")
        self.horizontalLayout_2.addWidget(self.LoadFiletoWidget1Button)
        self.ClearWidget1Button = QtWidgets.QPushButton(self.centralwidget)
        self.ClearWidget1Button.setObjectName("ClearWidget1Button")
        self.horizontalLayout_2.addWidget(self.ClearWidget1Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SavedData2Widget = PlotWidget(self.centralwidget)
        self.SavedData2Widget.setObjectName("SavedData2Widget")
        self.verticalLayout_4.addWidget(self.SavedData2Widget)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LoadFiletoWidget2Button = QtWidgets.QPushButton(self.centralwidget)
        self.LoadFiletoWidget2Button.setObjectName("LoadFiletoWidget2Button")
        self.horizontalLayout_3.addWidget(self.LoadFiletoWidget2Button)
        self.ClearWidget2Button = QtWidgets.QPushButton(self.centralwidget)
        self.ClearWidget2Button.setObjectName("ClearWidget2Button")
        self.horizontalLayout_3.addWidget(self.ClearWidget2Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
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
        self.LoadFiletoWidget1Button.setText(_translate("MainWindow", "Load A File"))
        self.ClearWidget1Button.setText(_translate("MainWindow", "Clear Plot"))
        self.LoadFiletoWidget2Button.setText(_translate("MainWindow", "Load A File"))
        self.ClearWidget2Button.setText(_translate("MainWindow", "Clear Plot"))

from pyqtgraph import PlotWidget
