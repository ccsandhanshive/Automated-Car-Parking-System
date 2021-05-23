# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import booking_db as db
import insertpy
from admin_login import Admin
from reg_succ import succ


class Ui_MainWindow(object):



    def setupUi(self, MainWindow,rto):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        import booking_db as t
        t.BookDB().InsertCancleBooking(self.dt, QtCore.QTime.currentTime().hour(), "---", "---")
        t.BookDB().InsertRTO(self.dt, QtCore.QTime.currentTime().hour(), "---", "---")
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        #self.MainLabel.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        #self.MainLabel.setFont(font)
        #self.MainLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
#"background-color: rgb(0, 0, 0);")
#        self.MainLabel.setObjectName("MainLabel")
        self.loginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(260, 430, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.loginbtn.setFont(font)
        self.loginbtn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.loginbtn.setObjectName("loginbtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 130, 81, 81))
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 210, 251, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../Downloads/lg5.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 310, 251, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../Downloads/lg6.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 70, 371, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../Downloads/lg9 - Copy.jpg"))
        self.label_4.setObjectName("label_4")
        self.passwordtext = QtWidgets.QLineEdit(self.centralwidget)

        self.passwordtext.setGeometry(QtCore.QRect(260, 360, 251, 41))
        self.passwordtext.setObjectName("passwordtext")
        self.passwordtext.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ulogintext = QtWidgets.QLineEdit(self.centralwidget)
        self.ulogintext.setGeometry(QtCore.QRect(260, 260, 251, 41))
        self.ulogintext.setObjectName("ulogintext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.timelable = QtWidgets.QLabel(self)
        #self.timelable.setText("hh:mm:yy")
        #self.timelable.setGeometry(260, 50, 500, 50)
        #self.timelable.setFont(QtCore.QFont("mangal_0", 20, QtCore.QFont.Bold))
        self.rto=rto
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.MainLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400; color:#ffffff;\">Slot Booked Successfully</span></p></body></html>"))
        self.loginbtn.setText(_translate("MainWindow", "LOGIN"))
        if self.rto==0:
            self.loginbtn.clicked.connect(self.check)
        if self.rto==1:
            self.loginbtn.clicked.connect(self.rtologin)
    def check(self):
        self.user=self.ulogintext.text()
        self.Pass=self.passwordtext.text()
        if self.ulogintext.text() == "admin" and self.passwordtext.text() == "admin":

            self.window = QtWidgets.QMainWindow()
            import adminpy
            self.ui = adminpy.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            '''self.window = QtWidgets.QMainWindow()
            self.ui = Admin()
            #self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(), QtCore.QDate.currentDate(), self.ST,
             #               self.STM, self.ET, self.ETM)
            self.window.show()
            MainWindow.hide()'''

            '''self.window = QMainWindow(self)
            self.ui = Admin()
            self.ui.show()
            self.hide()'''
        else:
            db.BookDB().CheckLogIn(self.user, self.Pass)
            db.BookDB().CheckCancleBook(self.user, self.Pass)
            no = db.BookDB().CheckLogIn(self.user, self.Pass)
            no2 = db.BookDB().CheckCancleBook(self.user, self.Pass)
            print("no is", no)
            if no != 1:
                db.BookDB.CheckRTO(self, self.user, self.Pass)
                no1 = db.BookDB.CheckRTO(self, self.user, self.Pass)
                print("no1 is", no1)
                if no1 == 1:
                    self.window = QtWidgets.QMainWindow()
                    import popup
                    self.ui = popup.Ui_MainWindow()
                    self.ui.setupUi(self.window,"------", "--------","You Are To Late So Please Go UNDERGROUND Section To Pick Up Your Car!!!")
                    self.window.show()
                    #self.ui = succ("------", "--------","You Are To Late So Please Go UNDERGROUND Section To Pick Up Your Car!!!")
                    # self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(), QtCore.QDate.currentDate(), self.ST,
                    #               self.STM, self.ET, self.ETM)
                    MainWindow.hide()

                    '''self.window = QMainWindow(self)
                    self.ui = succ("------", "--------","You Are To Late So Please Go UNDERGROUND Section To Pick Up Your Car!!!")
                    self.ui.show()
                    self.hide()'''
                if no1 != 1:
                    self.window = QtWidgets.QMainWindow()
                    import popup
                    self.ui = popup.Ui_MainWindow()
                    self.ui.setupUi(self.window,"------", "--------", "No Record Found")
                    self.window.show()
                    MainWindow.hide()
                    #self.ui = succ("------", "--------", "No Record Found")
                    # self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(), QtCore.QDate.currentDate(), self.ST,
                    #               self.STM, self.ET, self.ETM)


                    '''self.window = QMainWindow(self)
                    self.ui = succ("------", "--------", "No Record Found")
                    self.ui.show()
                    self.hide()'''
                if no2 == 1:
                    self.window = QtWidgets.QMainWindow()
                    import popup
                    self.ui = popup.Ui_MainWindow()
                    self.ui.setupUi(self.window, "------", "--------", "Sorry ,You Are To Late Please Again Book Your Slot!!!")
                    self.window.show()
                    #self.ui = succ("------", "--------", "Sorry ,You Are To Late Please Again Book Your Slot!!!")
                    # self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(), QtCore.QDate.currentDate(), self.ST,
                    #               self.STM, self.ET, self.ETM)
                    MainWindow.hide()

                    '''self.window = QMainWindow(self)
                    self.ui = succ("------", "--------", "Sorry ,You Are To Late Please Again Book Your Slot!!!")
                    self.ui.show()
                    self.hide()'''
            if no == 1:
                self.window = QtWidgets.QMainWindow()

                self.ui = insertpy.Ui_MainWindow()
                self.ui.setupUi(self.window,0, self.user, self.Pass)
                self.window.show()
                MainWindow.hide()

                '''self.window = QMainWindow(self)
                self.ui = insert(0, self.user, self.Pass)
                self.ui.show()
                self.hide()'''




    def rtologin(self):
        self.user = self.ulogintext.text()
        self.Pass = self.passwordtext.text()
        db.BookDB().CheckLogIn(self.user, self.Pass)
        no = db.BookDB().CheckRTO(self.user, self.Pass)
        print("no is", no)
        if no == 1:
            self.window = QtWidgets.QMainWindow()
            self.ui = insertpy.Ui_MainWindow()
            self.ui.setupUi(self.window,1,self.user, self.Pass)
            self.window.show()
            MainWindow.hide()

            '''self.window = QMainWindow(self)
            self.ui = insert(1,self.user, self.Pass)
            self.ui.show()
            self.hide()'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,0)
    MainWindow.show()
    sys.exit(app.exec_())

