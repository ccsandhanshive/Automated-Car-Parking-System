# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(160, 10, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.MainLabel.setFont(font)
        self.MainLabel.setObjectName("MainLabel")
        self.CreatLabel = QtWidgets.QLabel(self.centralwidget)
        self.CreatLabel.setGeometry(QtCore.QRect(260, 70, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CreatLabel.setFont(font)
        self.CreatLabel.setObjectName("CreatLabel")
        self.UserLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserLabel.setGeometry(QtCore.QRect(50, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UserLabel.setFont(font)
        self.UserLabel.setObjectName("UserLabel")
        self.UserEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserEdit.setGeometry(QtCore.QRect(300, 150, 451, 41))
        self.UserEdit.setObjectName("UserEdit")
        self.PassLabel = QtWidgets.QLabel(self.centralwidget)
        self.PassLabel.setGeometry(QtCore.QRect(50, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PassLabel.setFont(font)
        self.PassLabel.setObjectName("PassLabel")
        self.PassEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PassEdit.setGeometry(QtCore.QRect(300, 220, 451, 41))
        self.PassEdit.setObjectName("PassEdit")
        self.RePassLabel = QtWidgets.QLabel(self.centralwidget)
        self.RePassLabel.setGeometry(QtCore.QRect(50, 300, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.RePassLabel.setFont(font)
        self.RePassLabel.setObjectName("RePassLabel")
        self.RePassEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RePassEdit.setGeometry(QtCore.QRect(300, 290, 451, 41))
        self.RePassEdit.setObjectName("RePassEdit")
        self.LogUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogUpButton.setGeometry(QtCore.QRect(50, 360, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.LogUpButton.setFont(font)
        self.LogUpButton.setObjectName("LogUpButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.MainLabel.setText(_translate("MainWindow", "Sloat Booked Successfully"))
        self.CreatLabel.setText(_translate("MainWindow", "Create Your Login"))
        self.UserLabel.setText(_translate("MainWindow", "Username"))
        self.PassLabel.setText(_translate("MainWindow", "Password"))
        self.RePassLabel.setText(_translate("MainWindow", "Re-Enter Password"))
        self.LogUpButton.setText(_translate("MainWindow", "LOG UP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

