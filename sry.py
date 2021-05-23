# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sry.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtSql,QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget
        self.label.setGeometry(QtCore.QRect(160, 0, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 831, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 80, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 150, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableView(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 220, 581, 331))
        self.tableWidget.setObjectName("tableWidget")
        #self.tableWidget.setColumnCount(2)
        # self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        #self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
            #        self.tableWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 26))
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
        self.label.setText(_translate("MainWindow", "SRY NO SLOAT AVALABILE FOR YOUR TIME"))
        self.label_2.setText(_translate("MainWindow", " IF YOU CHANGE YOUR TIME THEN ITS POSSIBLE TO ALLOCATE SLOAT"))
        self.pushButton.setText(_translate("MainWindow", "CLICK HERE TO SHOW TIME AND SLOAT"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
#        item = self.tableWidget.horizontalHeaderItem(0)
        #        item.setText(_translate("MainWindow", "TIME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SLOAT"))
        self.setTab()

    def setTab(self):

        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("sampledb")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            self.tablemodel.setQuery("select * from booking")
            self.tableWidget.setModel(self.tablemodel)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

