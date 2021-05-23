# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sloat.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.S1 = QtWidgets.QPushButton(self.centralwidget)
        self.S1.setGeometry(QtCore.QRect(30, 10, 161, 91))
        self.S1.setObjectName("S1")
        self.S2 = QtWidgets.QPushButton(self.centralwidget)
        self.S2.setGeometry(QtCore.QRect(220, 10, 161, 91))
        self.S2.setObjectName("S2")
        self.S3 = QtWidgets.QPushButton(self.centralwidget)
        self.S3.setGeometry(QtCore.QRect(410, 10, 161, 91))
        self.S3.setObjectName("S3")
        self.S4 = QtWidgets.QPushButton(self.centralwidget)
        self.S4.setGeometry(QtCore.QRect(590, 10, 161, 91))
        self.S4.setObjectName("S4")
        self.S8 = QtWidgets.QPushButton(self.centralwidget)
        self.S8.setGeometry(QtCore.QRect(590, 120, 161, 91))
        self.S8.setObjectName("S8")
        self.S6 = QtWidgets.QPushButton(self.centralwidget)
        self.S6.setGeometry(QtCore.QRect(220, 120, 161, 91))
        self.S6.setObjectName("S6")
        self.s7 = QtWidgets.QPushButton(self.centralwidget)
        self.s7.setGeometry(QtCore.QRect(410, 120, 161, 91))
        self.s7.setObjectName("s7")
        self.S5 = QtWidgets.QPushButton(self.centralwidget)
        self.S5.setGeometry(QtCore.QRect(30, 120, 161, 91))
        self.S5.setObjectName("S5")
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(32, 267, 721, 51))
        self.select.setObjectName("select")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
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
        self.S1.setText(_translate("MainWindow", "Sloat 1"))
        self.S2.setText(_translate("MainWindow", "Sloat 2"))
        self.S3.setText(_translate("MainWindow", "Sloat 3"))
        self.S4.setText(_translate("MainWindow", "Sloat 4"))
        self.S8.setText(_translate("MainWindow", "Sloat 8"))
        self.S6.setText(_translate("MainWindow", "Sloat 6"))
        self.s7.setText(_translate("MainWindow", "Sloat 7"))
        self.S5.setText(_translate("MainWindow", "Sloat 5"))
        self.select.setText(_translate("MainWindow", "SELECT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

