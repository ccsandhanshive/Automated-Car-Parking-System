# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import booking_db as db
import cashpy
from cash_Back import Cash
from reg_succ import succ


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,rto,user,passw):
        MainWindow.setObjectName("MainWindow")


        self.rto=rto
        self.user=user
        self.passw=passw
        MainWindow.resize(790, 579)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 250, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 310, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 370, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.parkButton = QtWidgets.QPushButton(self.centralwidget)
        self.parkButton.setGeometry(QtCore.QRect(590, 200, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.parkButton.setFont(font)
        self.parkButton.setObjectName("parkButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(590, 490, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setObjectName("ExitButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 0, 20, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 50, 381, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./Images/6.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 280, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(410, 260, 431, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 310, 421, 171))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./Images/7.jpg"))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(510, 500, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.UserLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserLabel.setGeometry(QtCore.QRect(220, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.UserLabel.setFont(font)
        self.UserLabel.setObjectName("UserLabel")
        self.CarLabel = QtWidgets.QLabel(self.centralwidget)
        self.CarLabel.setGeometry(QtCore.QRect(220, 200, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.CarLabel.setFont(font)
        self.CarLabel.setObjectName("CarLabel")
        self.TimeStartShow = QtWidgets.QLabel(self.centralwidget)
        self.TimeStartShow.setGeometry(QtCore.QRect(220, 260, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TimeStartShow.setFont(font)
        self.TimeStartShow.setObjectName("TimeStartShow")
        self.TimeEndShow = QtWidgets.QLabel(self.centralwidget)
        self.TimeEndShow.setGeometry(QtCore.QRect(220, 320, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TimeEndShow.setFont(font)
        self.TimeEndShow.setObjectName("TimeEndShow")
        self.ShowCuuentTime = QtWidgets.QLabel(self.centralwidget)
        self.ShowCuuentTime.setGeometry(QtCore.QRect(220, 380, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ShowCuuentTime.setFont(font)
        self.ShowCuuentTime.setObjectName("ShowCuuentTime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        if rto==0:
            db.BookDB().CheckCar(user,passw)
            UserName,CarNo,TimeStart,TimeStartMin,TimeEnd,TimeEndMin=db.BookDB().CheckCar(user,passw)
        if rto==1:
            db.BookDB().LoginRTO(user, passw)
            UserName, CarNo, TimeStart, TimeStartMin, TimeEnd, TimeEndMin = db.BookDB().LoginRTO(user, passw)

        self.un=UserName
        self.cn=CarNo
        self.ts=TimeStart
        self.tsm=TimeStartMin
        self.te=TimeEnd
        self.tem=TimeEndMin
        print("username: {0}     car_no: {1}    time start : {2}   time end : {3}  ".format(self.un,self.cn,self.ts+":"+self.tsm,self.te+":"+self.tem))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.m=MainWindow
    def retranslateUi(self, MainWindow):
        QF = QtGui.QFont("Perpetua Titling MT", 14,QtGui.QFont.Bold)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">USER NAME </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">CAR NO </span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">TIME START </span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">TIME END </span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">CURRENT TIME</span></p></body></html>"))
        self.parkButton.setText(_translate("MainWindow", "PARK  CAR"))
        self.ExitButton.setText(_translate("MainWindow", "EXIT "))
        self.label_5.setText(_translate("MainWindow", "For parking the car"))
        self.label.setText(_translate("MainWindow", "PRESS ->"))
        self.label_7.setText(_translate("MainWindow", "For Exit from parking"))
        self.label_11.setText(_translate("MainWindow", "PRESS ->"))





        self.TimeStartShow.setText(_translate("MainWindow", str(str(self.ts) + ":" + str(self.tsm))))
        self.TimeEndShow.setText(_translate("MainWindow", str(str(self.te) + ":" + str(self.tem))))
        self.ShowCuuentTime.setText(_translate("MainWindow", QtCore.QTime.currentTime().toString("hh:mm")))
        self.TimeStartShow.setFont(QF)
        self.TimeEndShow.setFont(QF)
        self.ShowCuuentTime.setFont(QF)




        self.cnt = db.BookDB().CheckCarPark(self.cn)
        self.cnt1 = db.BookDB().CheckCarExit(self.cn)
        print("cnt ="+str(self.cnt))
        print("cnt1:"+str(self.cnt1))
        self.parkButton.setEnabled(False)
        self.ExitButton.setEnabled(False)
        if self.rto != 1:
            if self.cnt == 0:
                self.parkButton.setEnabled(True)
                self.parkButton.clicked.connect(self.Park)
        if self.cnt1 == 0 and self.cnt != 0 or self.rto == 1:
            self.ExitButton.setEnabled(True)
            self.ExitButton.clicked.connect(self.Exit)
        self.UserLabel.setText(self.un)
        self.CarLabel.setText(self.cn)
        self.UserLabel.setFont(QF)
        self.CarLabel.setFont(QF)

    def Park(self):
        db.BookDB().ParkCarInsert(self.un,self.cn,self.ts,self.tsm,self.te,self.tem)
        print("data park insert")
        self.m.hide()
        self.window = QtWidgets.QMainWindow()
        import popup
        self.ui = popup.Ui_MainWindow()
        self.ui.setupUi(self.window,"-------------","--------","car Park Successfully!!!!!!!!!!")
        self.window.show()
        #self.ui = succ("-------------","--------","car Park Successfully!!!!!!!!!!")



    def Exit(self):
        c=str(QtCore.QDate.currentDate().toString("dd-MM-yyyy"))
        print(c)
        db.BookDB().ParkCarExit(c,self.un,self.cn,self.ts,self.tsm,self.te,self.tem)

        print("data exit insert")
        db.BookDB().DeleteAllRecords(self.cn)

        if self.rto==0:
            self.m.hide()
            self.window = QtWidgets.QMainWindow()
            self.window = QtWidgets.QMainWindow()
            self.ui = cashpy.Ui_MainWindow()
            self.ui.setupUi(self.window,0,self.un,self.cn,self.te,self.tem)
            self.window.show()


        if self.rto==1:
            self.m.hide()
            self.window = QtWidgets.QMainWindow()
            self.ui = cashpy.Ui_MainWindow()
            self.ui.setupUi(self.window, 1, self.un, self.cn, self.te, self.tem)
            self.window.show()
            db.BookDB().DeleteRto(self.cn)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,0,"tar","tar123")
    MainWindow.show()
    sys.exit(app.exec_())

