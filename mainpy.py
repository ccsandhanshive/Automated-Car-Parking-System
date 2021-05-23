# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime

import book_pagepy as bookPage
import loginpy
import sys
import booking_db as t
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *

class Ui_MainWindow(object):		#Main Window
    def setupUi(self, MainWindow):
        MainWindow.setMaximumSize(QtCore.QSize(650,585))
        MainWindow.setMinimumSize(QtCore.QSize(650,585 ))
        from PyQt5.QtCore import QDate, QTime
        t.BookDB().InsertCancleBooking(QDate.currentDate().toString("dd-MM-yyyy"), QTime.currentTime().hour(), "---", "---") #check user late to park
        t.BookDB().InsertRTO(QDate.currentDate().toString("dd-MM-yyyy"), QTime.currentTime().hour(), "---", "---")	#check user late to receive
        self.t = CheckThered()
        self.t.check.connect(self.AutoCheck)
        self.t.start()
        #self.ui1=loginpy.Ui_MainWindow()
        #self.ui1=loginpy.Ui_MainWindow()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 585)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/images (5).jpg);\n"
                                 "background-image: url(./Images/mainpage.jpg);\n"
                                 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 270, 491, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(170, 85, 255);\n"
                                      "color: rgb(255, 255, 0);\n"
                                      "border-bottom-color: rgb(0, 0, 0);\n"
                                      "background-image: url(C:/Users/HP/Desktop/car.jpg);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 330, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-image: url(C:/Users/HP/Desktop/car.jpg);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 400, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(33, 33, 33);\n"
                                        "background-image: url(C:/Users/HP/Desktop/car.jpg);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 470, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 0, 0);\n"
                                        "background-image: url(C:/Users/HP/Desktop/car.jpg);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 631, 251))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("image: url(E:/new sd/Eraser/1536827617715.png);\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 661, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url(C:/Users/HP/Desktop/images.jpg);\n"
                                   "color: rgb(0, 0, 255);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        #self.concept = QtWidgets.QPushButton(MainWindow)
        #self.concept.setText("concept")
        #self.concept.setFont(QtGui.QFont("Perpetua Titling MT",6))
        #self.concept.setStyleSheet("color:blue")
        #self.concept.setGeometry(QtCore.QRect(592, 0, 61, 21))
        #self.demo=QtWidgets.QPushButton(MainWindow)
        #self.demo.setText("demo")

        #self.demo.setFont(QtGui.QFont("Perpetua Titling MT",6))
        #self.demo.setGeometry(QtCore.QRect(590, 20, 61, 21))
        #self.demo.setStyleSheet("color:blue")
        #self.full_demo=QtWidgets.QPushButton(MainWindow)
        #self.full_demo.setText("Full Demo")
        #self.full_demo.setFont(QtGui.QFont("Perpetua Titling MT",6))
        #self.full_demo.setStyleSheet("color:blue")
        #self.full_demo.setGeometry(QtCore.QRect(590, 40, 61, 21))
        #self.window.showEvent(MainWindow.hide())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.m=MainWindow
        #self.concept.clicked.connect(self.op)
        #self.demo.clicked.connect(self.op1)
        #self.full_demo.clicked.connect(self.op2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "BOOKING"))
        self.pushButton_2.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_3.setText(_translate("MainWindow", "UNDERGROUND"))
        self.pushButton_4.setText(_translate("MainWindow", "EXIT"))
        self.label_2.setText(_translate("MainWindow", "        AUTOMATED CAR PARKING SYSTEM"))
        self.pushButton.clicked.connect(self.book_in)
        self.pushButton_2.clicked.connect(self.login_in)
        self.pushButton_3.clicked.connect(self.rto_in)
        self.pushButton_4.clicked.connect(self.exit_in)


    def AutoCheck(self):		#check everytime
        t.BookDB().InsertCancleBooking(QDate.currentDate().toString("dd-MM-yyyy"), QtCore.QTime.currentTime().hour(), "---", "---")
        t.BookDB().InsertRTO(QDate.currentDate().toString("dd-MM-yyyy"),QtCore.QTime.currentTime().hour(),"---","---")
        print("run")

    def book_in(self):		#for booking
        self.m.hide()
        import  book_pagepy
        self.window = QtWidgets.QMainWindow()
        self.ui = book_pagepy.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def login_in(self):		#for login
        '''import loginpy1
        self.ui = loginpy1.Ui_MainWindow(0)
        self.ui.show()'''

        self.m.hide()
        import loginpy1
        self.window = QtWidgets.QMainWindow()
        self.ui = loginpy1.Ui_MainWindow()
        self.ui.setupUi(self.window,0)
        self.window.show()



        '''self.window = QtWidgets.QMainWindow()
        self.ui =login(0)
        self.ui.show()'''

    def  rto_in(self):				#underground
        self.m.hide()
        import loginpy1
        self.window = QtWidgets.QMainWindow()
        self.ui = loginpy1.Ui_MainWindow()
        self.ui.setupUi(self.window, 1)
        self.window.show()

        '''print("RTO LOGIN")
        self.window = QtWidgets.QMainWindow()
        self.ui = login(1)
        self.ui.show()'''

    def exit_in(self):			#for exit
        sys.exit()


    def op(self):				#for play vidio about concept
        import cv2
        cap = cv2.VideoCapture("E:/sd card/bluetooth/concept.mkv")

        ret, frame = cap.read()
        while (1):
            ret, frame = cap.read()

            cv2.imshow('frame', frame)

            if cv2.waitKey(13) & 0xFF == ord('q') or ret == False:
                cap.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow('frame', frame)
        cap.release()
        cv2.destroyAllWindows()

    def op1(self):			#for short demo vidio
        import cv2
        cap = cv2.VideoCapture("C:/Users/HP/Videos/demo.mp4")
        ret, frame = cap.read()
        while (1):
            ret, frame = cap.read()

            cv2.imshow('frame', frame)
            if cv2.waitKey(30) & 0xFF == ord('q') or ret == False:
                cap.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow('frame', frame)
        cap.release()
        cv2.destroyAllWindows()

    def op2(self):				#for long demo
        import cv2
        cap = cv2.VideoCapture("C:/Users/HP/Videos/full_demo.mp4")
        ret, frame = cap.read()
        while (1):
            ret, frame = cap.read()

            cv2.imshow('frame', frame)
            if cv2.waitKey(30) & 0xFF == ord('q') or ret == False:
                cap.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow('frame', frame)
        cap.release()
        cv2.destroyAllWindows()


class CheckThered(QtCore.QThread):		#check user late to receive car or park car
    check= QtCore.pyqtSignal()
    def run(self):
        while True:
            self.check.emit()
            QtCore.QThread.sleep(5)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())