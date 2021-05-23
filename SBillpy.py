# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SBillui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Time_Cal import getTime
from reg_succ import succ


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,sloat,UserEdit,CarEdit,ST,STM,ET,ETM):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 618)

        self.UserEdit1 = UserEdit
        self.cn1 = CarEdit
        self.st = ST;
        self.Smin = STM;
        self.et = ET;
        self.etm = ETM
        self.hrs, self.mins = getTime(str(ST) + ":" + str(STM), str(ET) + ":" + str(ETM))
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TotalTimeEdit = QtWidgets.QLabel(self.centralwidget)
        self.TotalTimeEdit.setGeometry(QtCore.QRect(490, 340, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TotalTimeEdit.setFont(font)
        self.TotalTimeEdit.setObjectName("TotalTimeEdit")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(240, 290, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(240, 340, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.ETimeEdit_2 = QtWidgets.QLabel(self.centralwidget)
        self.ETimeEdit_2.setGeometry(QtCore.QRect(490, 290, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ETimeEdit_2.setFont(font)
        self.ETimeEdit_2.setObjectName("ETimeEdit_2")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(240, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(240, 390, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(240, 190, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(240, 240, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.CarNoEdit = QtWidgets.QLabel(self.centralwidget)
        self.CarNoEdit.setGeometry(QtCore.QRect(490, 190, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CarNoEdit.setFont(font)
        self.CarNoEdit.setObjectName("CarNoEdit")
        self.UserNameEdit = QtWidgets.QLabel(self.centralwidget)
        self.UserNameEdit.setGeometry(QtCore.QRect(490, 140, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.UserNameEdit.setFont(font)
        self.UserNameEdit.setObjectName("UserNameEdit")
        self.rsedit = QtWidgets.QLabel(self.centralwidget)
        self.rsedit.setGeometry(QtCore.QRect(490, 390, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rsedit.setFont(font)
        self.rsedit.setObjectName("rsedit")
        self.StimeEdit = QtWidgets.QLabel(self.centralwidget)
        self.StimeEdit.setGeometry(QtCore.QRect(490, 240, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.StimeEdit.setFont(font)
        self.StimeEdit.setObjectName("StimeEdit")
        self.pay = QtWidgets.QPushButton(self.centralwidget)
        self.pay.setGeometry(QtCore.QRect(410, 440, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pay.setFont(font)
        self.pay.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pay.setObjectName("pay")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 40, 431, 61))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sloat1 = sloat
        self.rs = 0.0
        print(self.rs)
        self.rs = self.rs + float(self.hrs) * 10.00
        print(self.hrs)
        print(self.rs)
        self.rs = self.rs + float(self.mins) * 0.1666666667
        print(self.mins)
        print(self.rs)
        self.rs = round(self.rs)
        print(self.rs)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.m=MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TotalTimeEdit.setText(_translate("MainWindow",self.hrs+":"+self.mins ))
        self.label_15.setText(_translate("MainWindow", "End  Time           ->"))
        self.label_16.setText(_translate("MainWindow", "Total  Time          ->"))
        self.ETimeEdit_2.setText(_translate("MainWindow", str(str(self.et)+":"+str(self.etm))))
        self.label_19.setText(_translate("MainWindow", "User Name          ->"))
        self.label_20.setText(_translate("MainWindow", "Total Rs               ->"))
        self.label_21.setText(_translate("MainWindow", "Car No                ->"))
        self.label_22.setText(_translate("MainWindow", "Start Time           ->"))
        self.CarNoEdit.setText(_translate("MainWindow", self.cn1))
        self.UserNameEdit.setText(_translate("MainWindow",self.UserEdit1))
        self.rsedit.setText(_translate("MainWindow",str( self.rs)))
        self.StimeEdit.setText(_translate("MainWindow",str(str(self.st)+":"+str(self.Smin))))
        self.pay.setText(_translate("MainWindow", "PAY"))
        self.label.setText(_translate("MainWindow", "AUTO GENRATED BILL"))
        self.pay.clicked.connect(self.paid)
    def paid(self):			#for insert data into Payment table

        import booking_db as db

        db.BookDB().InsertPayment(QtCore.QDate.currentDate().toString("dd-MM-yyyy"), self.UserNameEdit.text(), self.CarNoEdit.text(), self.st,
                                  self.Smin, self.et, self.etm, self.hrs + ":" + self.mins, self.rs)
        self.m.hide()
        self.window = QtWidgets.QMainWindow()
        import popup
        self.ui = popup.Ui_MainWindow()
        self.ui.setupUi(self.window,self.cn1, self.sloat1, "PAY YOUR AMOUNT ON COUNTER!!!")
        self.window.show()

        #self.ui = succ(self.cn1, self.sloat1, "PAY YOUR AMOUNT ON COUNTER!!!")
        # self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(), QtCore.QDate.currentDate(), self.ST,
        #               self.STM, self.ET, self.ETM)




     #InsertPayment(self, date, username, carno, shour, smin, ehour, emin, totaltime, totalrs)
     #db.BookDB().InsertPayment(self.dateEdit.text(),self.UserNameEdit.text(),self.CarNoEdit.text(),self.st,self.Smin,self.et,self.etm,self.hrs+":"+self.mins,self.rs)
     #self.ui = succ(self.cn1,self.sloat1,"PAY YOUR AMOUNT ON COUNTER!!!")
     #self.ui.show()
     #self.hide()'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,"sloat_6","abc","mh40-8664","10","20","14","19")
    MainWindow.show()
    sys.exit(app.exec_())

