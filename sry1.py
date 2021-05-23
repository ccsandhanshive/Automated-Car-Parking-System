# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sry1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
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
        self.pushButton.setVisible(False)
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
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(110, 220, 591, 301))
        self.tableView.setObjectName("tableView")
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
        self.pushButton_2.clicked.connect(self.exit)
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
            self.tablemodel.setQuery("select b.TimeStart,b.TimeStartMin,b.TimeEnd,b.TimeEndMin,l.SloatNo from booking b,logup l where l.CarNo=b.CarNo")
            self.tableView.setModel(self.tablemodel)

    def exit(self):
        self.window = QtWidgets.QMainWindow()
        import MainFrame as m
        self.ui = m.Main()
        self.ui.show()
        #QtWidgets.MainWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

