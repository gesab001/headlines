# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app-gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import subprocess
import platform
from updateNews import getAllCurrentNews

class Ui_MainWindow(object):
    def updateNews(self):
        print("update news")
        getAllCurrentNews()
        

    def readNews(self):
        print("read news")
        webbrowser.open("read://https_www.stuff.co.nz/?url=https%3A%2F%2Fwww.stuff.co.nz%2Fnational%2Fpolitics%2F300411476%2Fcovid19-whole-country-could-see-restrictions-until-christmas-if-virus-isnt-stamped-out-in-auckland")

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 261, 151))
        self.groupBox.setObjectName("groupBox")
        self.update_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.update_pushButton.setGeometry(QtCore.QRect(50, 40, 161, 81))
        self.update_pushButton.setObjectName("update_pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 50, 311, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.read_pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.read_pushButton_2.setGeometry(QtCore.QRect(70, 40, 181, 71))
        self.read_pushButton_2.setObjectName("read_pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionupdateNews = QtWidgets.QAction(MainWindow)
        self.actionupdateNews.setObjectName("actionupdateNews")
        self.actionread = QtWidgets.QAction(MainWindow)
        self.actionread.setObjectName("actionread")

        self.retranslateUi(MainWindow)
        self.update_pushButton.clicked.connect(self.updateNews)
        self.read_pushButton_2.clicked.connect(self.readNews)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Update"))
        self.update_pushButton.setText(_translate("MainWindow", "Update"))
        self.groupBox_2.setTitle(_translate("MainWindow", "View"))
        self.read_pushButton_2.setText(_translate("MainWindow", "Read"))
        self.actionupdateNews.setText(_translate("MainWindow", "updateNews"))
        self.actionread.setText(_translate("MainWindow", "read"))
