# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slotui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import SBillpy
import booking_db as t
import srypy
from Start_Bill import SBill


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,user,CarNo,Date,STime,STimeM,ETime,ETimeM):
        MainWindow.setObjectName("MainWindow")
        self.t = CheckThered()
        self.t.check.connect(self.AutoCheck)
        self.t.start()
        self.un=user
        self.cn = CarNo
        self.dt = Date
        self.S = int(STime)
        self.SM = int(STimeM)
        self.e = int(ETime)
        self.em = int(ETimeM)
        MainWindow.resize(1258, 751)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-image: url(./Images/4.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 0, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.s1 = QtWidgets.QPushButton(self.centralwidget)
        self.s1.setGeometry(QtCore.QRect(30, 110, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.s1.setFont(font)
        self.s1.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")
        self.s1.setObjectName("s1")
        self.s2 = QtWidgets.QPushButton(self.centralwidget)
        self.s2.setGeometry(QtCore.QRect(330, 110, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.s2.setFont(font)
        self.s2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")
        self.s2.setObjectName("s2")
        self.s3 = QtWidgets.QPushButton(self.centralwidget)
        self.s3.setGeometry(QtCore.QRect(630, 110, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.s3.setFont(font)
        self.s3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")
        self.s3.setObjectName("s3")
        self.s4 = QtWidgets.QPushButton(self.centralwidget)
        self.s4.setGeometry(QtCore.QRect(930, 110, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.s4.setFont(font)
        self.s4.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")
        self.s4.setObjectName("s4")
        self.s5 = QtWidgets.QPushButton(self.centralwidget)
        self.s5.setGeometry(QtCore.QRect(30, 370, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.s5.setFont(font)
        self.s5.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")
        self.s5.setObjectName("s5")
        self.s6 = QtWidgets.QPushButton(self.centralwidget)
        self.s6.setGeometry(QtCore.QRect(330, 370, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.s6.setFont(font)
        self.s6.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")
        self.s6.setObjectName("s6")
        self.s8 = QtWidgets.QPushButton(self.centralwidget)
        self.s8.setGeometry(QtCore.QRect(940, 370, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.s8.setFont(font)
        self.s8.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")
        self.s8.setObjectName("s8")
        self.s7 = QtWidgets.QPushButton(self.centralwidget)
        self.s7.setGeometry(QtCore.QRect(630, 370, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.s7.setFont(font)
        self.s7.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")
        self.s7.setObjectName("s7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1258, 26))
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
        self.label.setText(_translate("MainWindow", "BOOK THE SLOTS HERE"))
        self.s1.setText(_translate("MainWindow", "SLOT 1"))
        self.s2.setText(_translate("MainWindow", "SLOT 2"))
        self.s3.setText(_translate("MainWindow", "SLOT 3"))
        self.s4.setText(_translate("MainWindow", "SLOT 4"))
        self.s5.setText(_translate("MainWindow", "SLOT 5"))
        self.s6.setText(_translate("MainWindow", "SLOT 6"))
        self.s8.setText(_translate("MainWindow", "SLOT 8"))
        self.s7.setText(_translate("MainWindow", "SLOT 7"))
        self.s1.clicked.connect(self.s1F)
        self.s2.clicked.connect(self.s2F)
        self.s3.clicked.connect(self.s3F)
        self.s4.clicked.connect(self.s4F)
        self.s5.clicked.connect(self.s5F)
        self.s6.clicked.connect(self.s6F)
        self.s7.clicked.connect(self.s7F)
        self.s8.clicked.connect(self.s8F)
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(122, 567, 921, 51))


        self.select.setText("Click here for see time and slot")
        self.select.setFont(QtGui.QFont("Perpetua Titling MT",20,QtGui.QFont.Bold))
        self.select.hide()

        self.m=MainWindow
        self.AutoCheck()


    def AutoCheck(self):			#check slot is booked or not if booked then this slot is invisible to user or visible and ready to book
        t.BookDB().InsertCancleBooking(self.dt, QtCore.QTime.currentTime().hour(), "---", "---")
        t.BookDB().InsertRTO(self.dt,QtCore.QTime.currentTime().hour(),"---","---")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_1")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_1")
        if a != 0:
            #self.s1.setStyleSheet("background-color: red")
            self.s1.hide()
        else:
            self.s1.show()
        print("Sloat 1")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_2")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_2")
        if a != 0:
            #self.s2.setStyleSheet("background-color: red")
            self.s2.hide()
        else:
            self.s2.show()
        print("Sloat 2")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_3")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_3")
        if a != 0:
            #self.s3.setStyleSheet("background-color: red")
            self.s3.hide()
        else:
            self.s3.show()
        print("Sloat 3")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_4")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_4")
        if a != 0:
            #self.s4.setStyleSheet("background-color: red")
            self.s4.hide()
        else:
            self.s4.show()
        print("Sloat 4")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_5")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_5")
        if a != 0:
            #self.s5.setStyleSheet("background-color: red")
            self.s5.hide()
        else:
            self.s5.show()
        print("Sloat 5")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_6")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_6")
        if a != 0:
            #self.s6.setStyleSheet("background-color: red")
            self.s6.hide()
        else:
            self.s6.show()
        print("Sloat 6")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_7")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_7")
        if a != 0:
            #self.s7.setStyleSheet("background-color: red")
            self.s7.hide()
        else:
            self.s7.show()
        print("Sloat 7")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_8")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_8")
        if a != 0:
            #self.s8.setStyleSheet("background-color: red")
            self.s8.hide()
        else:
            self.s8.show()
            print("Sloat 8")



    def s1F(self):		#slot 1 booking after booking there backgroud color change with red
        t.BookDB().insertSloat(self.cn, self.dt, self.S,self.SM, self.e,self.em,"sloat_1")
        self.s1.setStyleSheet("background-color: red")

        print("Sloat 1")
        self.Log_up("sloat_1")

    def s2F(self):		#slot 2 booking after booking there backgroud color change with red
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_2")
        self.s2.setStyleSheet("background-color: red")
        print("Sloat 2")
        self.Log_up("sloat_2")

    def s3F(self):		#slot 3 booking after booking there backgroud color change with red
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_3")
        self.s3.setStyleSheet("background-color: red")
        print("Sloat 3")
        self.Log_up("sloat_3")

    def s4F(self):		#slot 4 booking after booking there backgroud color change with red
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_4")
        self.s4.setStyleSheet("background-color: red")
        print("Sloat 4")
        self.Log_up("sloat_4")

    def s5F(self):		#slot 5 booking after booking there backgroud color change with red
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_5")
        self.s5.setStyleSheet("background-color: red")
        print("Sloat 5")
        self.Log_up("sloat_5")

    def s6F(self):		#slot 6 booking after booking there backgroud color change with red
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_6")
        self.s6.setStyleSheet("background-color: red")
        print("Sloat 6")
        self.Log_up("sloat_6")

    def s7F(self):		#slot 7 booking after booking there backgroud color change with red
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_7")
        self.s7.setStyleSheet("background-color: red")
        print("Sloat 7")
        self.Log_up("sloat_7")

    def s8F(self):		#slot 8 booking after booking there backgroud color change with red
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_8")
        self.s8.setStyleSheet("background-color: red")
        print("Sloat 8")
        self.Log_up("sloat_8")

    def Log_up(self,sloat):		#show logup window
        self.m.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = SBillpy.Ui_MainWindow()
        self.ui.setupUi(self.window , sloat , self.un, self.cn, self.S, self.SM, self.e, self.em)
        self.window.show()
        import book_pagepy
    def set(self):			#if all slot book
        if self.s1.isVisible() == False and self.s2.isVisible() == False and self.s3.isVisible() == False and self.s4.isVisible() == False and self.s5.isVisible() == False and self.s6.isVisible() == False and self.s7.isVisible() == False and self.s8.isVisible() == False:
            self.select.setVisible(True)





        '''self.window1 = QMainWindow(self)
        self.ui1 = SBill(sloat,self.un, self.cn, self.S, self.SM, self.e, self.em)
        self.ui1.show()
        self.hide()'''
    def jump(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = srypy.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.m.hide()

class CheckThered(QtCore.QThread):
    check= QtCore.pyqtSignal()
    def run(self):
        while True:
            self.check.emit()
            QtCore.QThread.sleep(5)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,"dhdjnfk","jhkjdshfiiu","02-10-2018","12","00","18","00")
    MainWindow.show()
    sys.exit(app.exec_())

