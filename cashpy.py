# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cashui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import booking_db as db
from Time_Cal import getTime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,rto,usernm,carno,endtimehour,endtimemin):
        self.rto=rto
        self.usernm=usernm
        self.carno=carno

        self.endtimehour=endtimehour
        self.endtimemin=endtimemin
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 512)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CashLabel = QtWidgets.QLabel(self.centralwidget)
        self.CashLabel.setGeometry(QtCore.QRect(130, 0, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CashLabel.setFont(font)
        self.CashLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.CashLabel.setObjectName("CashLabel")
        self.UserName = QtWidgets.QLabel(self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(10, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.UserName.setFont(font)
        self.UserName.setObjectName("UserName")
        self.CarNo = QtWidgets.QLabel(self.centralwidget)
        self.CarNo.setGeometry(QtCore.QRect(10, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.CarNo.setFont(font)
        self.CarNo.setObjectName("CarNo")
        self.ERime = QtWidgets.QLabel(self.centralwidget)
        self.ERime.setGeometry(QtCore.QRect(10, 180, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.ERime.setFont(font)
        self.ERime.setObjectName("ERime")
        self.CTime = QtWidgets.QLabel(self.centralwidget)
        self.CTime.setGeometry(QtCore.QRect(10, 230, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.CTime.setFont(font)
        self.CTime.setObjectName("CTime")








        self.RTime = QtWidgets.QLabel(self.centralwidget)
        self.RTime.setGeometry(QtCore.QRect(10, 280, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.RTime.setFont(font)
        self.RTime.setObjectName("RTime")
        self.CashbackRs = QtWidgets.QLabel(self.centralwidget)
        self.CashbackRs.setGeometry(QtCore.QRect(10, 330, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.CashbackRs.setFont(font)
        self.CashbackRs.setObjectName("CashbackRs")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(0, 380, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn.setFont(font)
        self.btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.btn.setObjectName("btn")
        self.UserNameEdit = QtWidgets.QLabel(self.centralwidget)
        self.UserNameEdit.setGeometry(QtCore.QRect(260, 80, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.UserNameEdit.setFont(font)
        self.UserNameEdit.setObjectName("UserNameEdit")
        self.CarNoEdit = QtWidgets.QLabel(self.centralwidget)
        self.CarNoEdit.setGeometry(QtCore.QRect(260, 130, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CarNoEdit.setFont(font)
        self.CarNoEdit.setObjectName("CarNoEdit")
        self.ETimeEdit = QtWidgets.QLabel(self.centralwidget)
        self.ETimeEdit.setGeometry(QtCore.QRect(260, 180, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ETimeEdit.setFont(font)
        self.ETimeEdit.setObjectName("ETimeEdit")
        self.CTimeEdit = QtWidgets.QLabel(self.centralwidget)
        self.CTimeEdit.setGeometry(QtCore.QRect(260, 230, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CTimeEdit.setFont(font)
        self.CTimeEdit.setObjectName("CTimeEdit")
        self.RTimeEdit = QtWidgets.QLabel(self.centralwidget)
        self.RTimeEdit.setGeometry(QtCore.QRect(260, 280, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CTimeEdit.setText(QtCore.QTime.currentTime().toString("hh-mm"))
        self.CTimeEdit.text().split(":")
        self.currentHour = self.CTimeEdit.text()[0] + self.CTimeEdit.text()[1]
        self.currentMin = self.CTimeEdit.text()[3] + self.CTimeEdit.text()[4]
        self.Current = self.currentHour + ":" + self.currentMin

        self.hr = endtimehour
        self.min = endtimemin
        self.time = self.hr + ":" + self.min
        self.time = endtimehour + ":" + endtimemin
        print("Current time is"+self.Current)
        print("specified time is"+self.time)
        if rto == 0:
            getTime(self.Current, self.time)
            self.ReHours, self.ReMin = getTime(self.Current, self.time)
        if rto == 1:
            getTime(self.time, self.Current)
            self.ReHours, self.ReMin = getTime(self.time, self.Current)
        print(self.ReHours)
        print(self.ReMin)
        print(self.currentHour)
        print(self.currentMin)
        self.crs = 0.0
        if rto == 0:
            try:
                self.crs = float(self.crs) + float(self.ReHours) * 10.00
                self.crs = float(self.crs) + float(self.ReMin) * 0.1666666667
            except:
                print("Exeception")
        if rto == 1:
            try:
                self.crs = float(self.crs) + float(self.ReHours) * 15.50
                self.crs = float(self.crs) + float(self.ReMin) * 0.2583333333
            except:
                print("Exeception")

        self.crs = round(self.crs)

        if rto == 0:
            if self.crs > 10.00:
                self.crs = 10.00

        self.RTimeEdit.setFont(font)
        self.RTimeEdit.setObjectName("RTimeEdit")
        self.CashbackRsEdit = QtWidgets.QLabel(self.centralwidget)
        self.CashbackRsEdit.setGeometry(QtCore.QRect(260, 330, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CashbackRsEdit.setFont(font)
        self.CashbackRsEdit.setObjectName("CashbackRsEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 26))
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
        if self.rto==0:
            self.CashLabel.setText(_translate("MainWindow", "CASHBACK"))
        if self.rto ==1:
            self.CashLabel.setText(_translate("MainWindow", "SURCHARGE"))
        self.UserName.setText(_translate("MainWindow", "User Name          ->"))
        self.CarNo.setText(_translate("MainWindow", "Car No                ->"))
        self.ERime.setText(_translate("MainWindow", "End Time            ->"))
        self.CTime.setText(_translate("MainWindow", "Current Time       ->"))
        if self.rto == 0:
            self.RTime.setText(_translate("MainWindow", "Remaining Time   ->"))
            self.CashbackRs.setText(_translate("MainWindow", "Cashback             ->"))
            self.btn.setText(_translate("MainWindow", "COLLECT AMOUNT FROM COUNTER"))
        if self.rto == 1:
            self.RTime.setText(_translate("MainWindow", "Extra Time   ->"))
            self.CashbackRs.setText(_translate("MainWindow", "Extra Amount             ->"))
            self.btn.setText(_translate("MainWindow", "PAY AMOUNT ON COUNTER"))
        self.UserNameEdit.setText(_translate("MainWindow", self.usernm))
        self.CarNoEdit.setText(_translate("MainWindow", self.carno))
        self.ETimeEdit.setText(_translate("MainWindow", self.endtimehour+":"+self.endtimemin))
        self.CTimeEdit.setText(_translate("MainWindow",QtCore.QTime.currentTime().toString("hh:mm") ))
        self.RTimeEdit.setText(_translate("MainWindow", self.ReHours+":"+self.ReMin))
        self.CashbackRsEdit.setText(_translate("MainWindow",str(self.crs)))
        self.btn.clicked.connect(self.ex)
    def ex(self):
        db.BookDB().InsertCashBack(self.usernm,self.carno,self.endtimehour+":"+self.endtimemin,self.currentHour + ":" + self.currentMin, self.ReHours + ":" + self.ReMin, self.crs)
        print("data sucessfully insert in cashback")
        db.BookDB().updateRTO(self.carno,self.ReHours+":"+self.ReMin,self.crs)
        print("All Records Deleted Succesfully!!")
        self.m.hide()
        self.window = QtWidgets.QMainWindow()
        import popup
        self.ui = popup.Ui_MainWindow()
        self.ui.setupUi(self.window,"-------------", "--------", "Car exit Success!!!!!!!!!!")
        self.window.show()
        #self.ui = s.succ("-------------", "--------", "Car exit Success!!!!!!!!!!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,0,"abc","mh30-2762","18","20")
    MainWindow.show()
    sys.exit(app.exec_())

