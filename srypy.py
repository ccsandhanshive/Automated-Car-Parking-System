# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sryui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 644)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 14pt \"Bahnschrift SemiBold\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 831, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: italic 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 520, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(110, 90, 691, 411))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.m=MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                 SRY NO SLOAT AVALABILE FOR YOUR TIME"))
        self.label_2.setText(_translate("MainWindow", "               IF YOU CHANGE YOUR TIME THEN ITS POSSIBLE TO ALLOCATE SLOT"))
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
            self.tablemodel.setQuery(
                "select b.TimeStart,b.TimeStartMin,b.TimeEnd,b.TimeEndMin,l.SloatNo from booking b,logup l where l.CarNo=b.CarNo")
            self.tableView.setModel(self.tablemodel)

    def exit(self):
        self.m.hide()
        self.window = QtWidgets.QMainWindow()
        import mainpy
        self.ui = mainpy.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

