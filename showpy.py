# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,old):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 553)
        import booking_db as t
        t.BookDB().InsertCancleBooking(QtCore.QDate.currentDate().toString("dd-MM-yyyy"), QtCore.QTime.currentTime().hour(), "---", "---") #check user late to park or receive car
        t.BookDB().InsertRTO(QtCore.QDate.currentDate().toString("dd-MM-yyyy"), QtCore.QTime.currentTime().hour(), "---", "---")
        self.old=old
        QF = QtGui.QFont("Perpetua Titling MT", 12)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Lucida Fax\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(490, 20, 16, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.booking = QtWidgets.QPushButton(self.centralwidget)
        self.booking.setGeometry(QtCore.QRect(10, 80, 111, 28))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.booking.setFont(font)
        self.booking.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"\n"
"\n"
"")
        self.booking.setObjectName("booking")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 30, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 14pt \"Lucida Fax\";\n"
"color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 80, 71, 21))
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.CarNoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CarNoEdit.setGeometry(QtCore.QRect(590, 80, 121, 22))
        self.CarNoEdit.setObjectName("CarNoEdit")
        self.CarNoEdit.setFont(QF)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 180, 691, 301))
        self.tableView.setObjectName("tableView")
        self.canclebooking = QtWidgets.QPushButton(self.centralwidget)
        self.canclebooking.setGeometry(QtCore.QRect(130, 80, 111, 28))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.canclebooking.setFont(font)
        self.canclebooking.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"\n"
"")
        self.canclebooking.setObjectName("canclebooking")
        self.exitcar = QtWidgets.QPushButton(self.centralwidget)
        self.exitcar.setGeometry(QtCore.QRect(250, 80, 121, 28))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.exitcar.setFont(font)
        self.exitcar.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"")
        self.exitcar.setObjectName("exitcar")
        self.logup = QtWidgets.QPushButton(self.centralwidget)
        self.logup.setGeometry(QtCore.QRect(380, 80, 111, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.logup.setFont(font)
        self.logup.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"")
        self.logup.setObjectName("logup")
        self.parkcar = QtWidgets.QPushButton(self.centralwidget)
        self.parkcar.setGeometry(QtCore.QRect(10, 120, 111, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parkcar.setFont(font)
        self.parkcar.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"")
        self.parkcar.setObjectName("parkcar")
        self.payment = QtWidgets.QPushButton(self.centralwidget)
        self.payment.setGeometry(QtCore.QRect(130, 120, 111, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.payment.setFont(font)
        self.payment.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"")
        self.payment.setObjectName("payment")
        self.underground = QtWidgets.QPushButton(self.centralwidget)
        self.underground.setGeometry(QtCore.QRect(250, 120, 121, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.underground.setFont(font)
        self.underground.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"")
        self.underground.setObjectName("underground")
        self.cashback = QtWidgets.QPushButton(self.centralwidget)
        self.cashback.setGeometry(QtCore.QRect(380, 120, 111, 28))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cashback.setFont(font)
        self.cashback.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"")
        self.cashback.setObjectName("cashback")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 361, 21))
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.booking_9 = QtWidgets.QPushButton(self.centralwidget)
        self.booking_9.setGeometry(QtCore.QRect(510, 120, 201, 28))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.booking_9.setFont(font)
        self.booking_9.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"")
        self.booking_9.setObjectName("booking_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 0, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 85, 0);\n"
"font: 16pt \"NSimSun\";\n"
"font: 14pt \"Lucida Fax\";")
        self.label_5.setObjectName("label_5")
        self.CarNoEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.CarNoEdit1.setGeometry(QtCore.QRect(370, 40, 121, 22))
        self.CarNoEdit1.setObjectName("CarNoEdit1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 40, 71, 21))
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.CarNoEdit1.setFont(QF)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TABLE INFORMATION"))
        self.booking.setText(_translate("MainWindow", "BOOKING"))
        self.label_2.setText(_translate("MainWindow", "DELETE RECORD"))
        self.label_3.setText(_translate("MainWindow", "CAR NO.:-"))
        self.canclebooking.setText(_translate("MainWindow", "CANCELBOOK"))
        self.exitcar.setText(_translate("MainWindow", "EXITCAR"))
        self.logup.setText(_translate("MainWindow", "LOGUP"))
        self.parkcar.setText(_translate("MainWindow", "PARKCAR"))
        self.payment.setText(_translate("MainWindow", "PAYMENT"))
        self.underground.setText(_translate("MainWindow", "UNDERGROUND"))
        self.cashback.setText(_translate("MainWindow", "CASHBACK"))
        self.label_4.setText(_translate("MainWindow", "[Please select above buttons to get details of paritucar table]"))
        self.booking_9.setText(_translate("MainWindow", "DELETE RECORD"))
        self.label_5.setText(_translate("MainWindow", "INFORMATION TO ADMIN"))
        self.label_6.setText(_translate("MainWindow", "CAR NO.:-"))
        self.booking.clicked.connect(self.BookingShow)
        self.canclebooking.clicked.connect(self.CancleBokkingShow)
        self.exitcar.clicked.connect(self.exitCarShow)
        self.logup.clicked.connect(self.LogUpShow)
        self.parkcar.clicked.connect(self.ParkCarShow)
        self.payment.clicked.connect(self.PaymentShow)
        self.underground.clicked.connect(self.UdergroundShow)
        self.cashback.clicked.connect(self.CashbackShow)
        self.booking_9.clicked.connect(self.Delete)
        if self.old == 1:
            self.booking_9.setEnabled(False)

    def BookingShow(self):			#for show all data from booking table
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old == 0:		#for current table
            self.db.setDatabaseName("sampledb")
        if self.old == 1:			#for history table
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select * from booking"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def CancleBokkingShow(self):  #for show cancle booking table data
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        if self.old == 0:			#current
            self.db.setDatabaseName("sampledb")
        if self.old == 1:			#history
            self.db.setDatabaseName("sampledb1")
        self.db.setUserName("root")
        self.db.setPassword("")
        print("ass")
        self.db.open()
        print(self.db.lastError().text())
        if (self.db.open()):
            print("Helo")
            self.tablemodel = QtSql.QSqlQueryModel()
            select = "select * from canclebooking"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def exitCarShow(self):			#for show all data from exitCar table
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
            select = "select * from exitcar"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def LogUpShow(self):		#for show logup table password is hide
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
            select = "select UserName,CarNo,SloatNo from logup"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def ParkCarShow(self):				#for show car park data
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
            select = "select * from parkcar"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def PaymentShow(self):				#for show all Payment data
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
            select = "select * from payment"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def UdergroundShow(self):			#for show underground data
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
            select = "select date,username,carno,start_hour,start_min,end_hour,end_min,extra_time,extra_rs from rto_payment"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def CashbackShow(self):					#for show cashback table data
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
            select = "select * from cashback"
            if self.CarNoEdit1.text() != "":
                select = select + " where CarNo='{}'".format(str(self.CarNoEdit1.text()))
                print(select)
            self.tablemodel.setQuery(select)
            self.tableView.setModel(self.tablemodel)

    def Delete(self):					#for delete data of perticuler car no
        import booking_db as t
        t.BookDB().DeleteAllRecords(str(self.CarNoEdit.text()))
        print("R    e   c   o   r   d")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,1)
    MainWindow.show()
    sys.exit(app.exec_())

