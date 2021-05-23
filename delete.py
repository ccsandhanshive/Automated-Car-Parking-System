# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import booking_db as t

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,old):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        QF = QtGui.QFont("Perpetua Titling MT", 14)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 281, 31))
        self.label1=QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(300,35, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label1.setFont(QtGui.QFont("mangal_0",11))
        self.label1.setObjectName("label1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(530, 30, 16, 151))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.booking = QtWidgets.QPushButton(self.centralwidget)
        self.booking.setGeometry(QtCore.QRect(10, 80, 93, 28))
        self.booking.setObjectName("booking")
        self.canclebooking = QtWidgets.QPushButton(self.centralwidget)
        self.canclebooking.setGeometry(QtCore.QRect(130, 80, 111, 28))
        self.canclebooking.setObjectName("canclebooking")
        self.exitcar = QtWidgets.QPushButton(self.centralwidget)
        self.exitcar.setGeometry(QtCore.QRect(278, 80, 101, 28))
        self.exitcar.setObjectName("exitcar")
        self.logup = QtWidgets.QPushButton(self.centralwidget)
        self.logup.setGeometry(QtCore.QRect(420, 80, 111, 28))
        self.logup.setObjectName("logup")
        self.parkcar = QtWidgets.QPushButton(self.centralwidget)
        self.parkcar.setGeometry(QtCore.QRect(10, 120, 93, 28))
        self.parkcar.setObjectName("parkcar")
        self.payment = QtWidgets.QPushButton(self.centralwidget)
        self.payment.setGeometry(QtCore.QRect(130, 120, 111, 28))
        self.payment.setObjectName("payment")
        self.underground = QtWidgets.QPushButton(self.centralwidget)
        self.underground.setGeometry(QtCore.QRect(280, 120, 101, 28))
        self.underground.setObjectName("underground")
        self.cashback = QtWidgets.QPushButton(self.centralwidget)
        self.cashback.setGeometry(QtCore.QRect(420, 120, 111, 28))
        self.cashback.setObjectName("cashback")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 80, 71, 21))
        self.label_3.setObjectName("label_3")
        self.CarNoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CarNoEdit.setFont(QF)
        self.CarNoEdit.setGeometry(QtCore.QRect(620, 80, 113, 22))
        self.CarNoEdit.setObjectName("CarNoEdit")
        self.CarNoEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.CarNoEdit1.setGeometry(QtCore.QRect(375,35,113,22))
        self.CarNoEdit1.setObjectName("CarNoEdit1")
        self.CarNoEdit1.setFont(QF)
        self.DeleteRecord = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteRecord.setGeometry(QtCore.QRect(550, 130, 250, 28))
        self.DeleteRecord.setObjectName("DeleteRecord")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 180, 791, 381))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.old=old
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SHOW TABLES"))
        self.label1.setText(_translate("MainWindow","Car No.:-"))
        self.booking.setText(_translate("MainWindow", "BOOKING"))
        self.canclebooking.setText(_translate("MainWindow", "CANCLEBOOKING"))
        self.exitcar.setText(_translate("MainWindow", "EXITCAR"))
        self.logup.setText(_translate("MainWindow", "LOGUP"))
        self.parkcar.setText(_translate("MainWindow", "PARKCAR"))
        self.payment.setText(_translate("MainWindow", "PAYMENT"))
        self.underground.setText(_translate("MainWindow", "UNDERGROUND"))
        self.cashback.setText(_translate("MainWindow", "CASHBACK"))
        self.label_2.setText(_translate("MainWindow", "DELETE RECORD"))
        self.label_3.setText(_translate("MainWindow", "CAR NO.:-"))
        self.DeleteRecord.setText(_translate("MainWindow", "DELETE RECORD"))
        self.booking.clicked.connect(self.BookingShow)
        self.canclebooking.clicked.connect(self.CancleBokkingShow)
        self.exitcar.clicked.connect(self.exitCarShow)
        self.logup.clicked.connect(self.LogUpShow)
        self.parkcar.clicked.connect(self.ParkCarShow)
        self.payment.clicked.connect(self.PaymentShow)
        self.underground.clicked.connect(self.UdergroundShow)
        self.cashback.clicked.connect(self.CashbackShow)
        self.DeleteRecord.clicked.connect(self.Delete)
        if self.old==1:
            self.DeleteRecord.setEnabled(False)			#visible if there needed
    def BookingShow(self):							#show all data present in booking table
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old==0:								
            self.db.setDatabaseName("sampledb")			#current booking table
        if self.old==1:
            self.db.setDatabaseName("sampledb1")		#history booking table
        self.db.setUserName("root")
        self.db.setPassword("")
       # print("ass")
        self.db.open()
        #print(self.db.lastError().text())
        if (self.db.open()):
         #   print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select * from booking"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))	#select car no for search perticuler car details
                #print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def CancleBokkingShow(self):						#select data from current cancle booking
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old == 0:
            self.db.setDatabaseName("sampledb")
        if self.old == 1:
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select="select * from canclebooking"
            if self.CarNoEdit1.text()!="":
                select=select+" where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)


    def exitCarShow(self):									#retrive data from exitcar table
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old==0:
            self.db.setDatabaseName("sampledb")
        if self.old==1:
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select * from exitcar"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def LogUpShow(self):							#retrive data from logup table
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old==0:
            self.db.setDatabaseName("sampledb")
        if self.old==1:
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select UserName,CarNo,SloatNo from logup"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)


    def ParkCarShow(self):								#retrive data from Parkcar table
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old==0:
            self.db.setDatabaseName("sampledb")
        if self.old==1:
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select * from parkcar"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def PaymentShow(self):									#retrive data from payment table
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old==0:
            self.db.setDatabaseName("sampledb")
        if self.old==1:
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select * from payment"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def UdergroundShow(self):									#retrive data from underground table
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old==0:
            self.db.setDatabaseName("sampledb")
        if self.old==1:
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select date,username,carno,start_hour,start_min,end_hour,end_min,extra_time,extra_rs from rto_payment"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def CashbackShow(self):							#retrive data from cashback table
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old==0:
            self.db.setDatabaseName("sampledb")
        if self.old==1:
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select * from cashback"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)
    def Delete(self):									#delete all records releted to selected car from current tables
        t.BookDB().DeleteAllRecords(str(self.CarNoEdit.text()))
        print("R    e   c   o   r   d")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,0)
    MainWindow.show()
    sys.exit(app.exec_())

