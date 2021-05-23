# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpy1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime

import booking_db as db
class Ui_MainWindow(object):
    def setupUi(self, MainWindow,rto):
        self.rto=rto

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        QF = QtGui.QFont("Perpetua Titling MT", 14)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogUpButton.setGeometry(QtCore.QRect(270, 450, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.LogUpButton.setFont(font)
        self.LogUpButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.LogUpButton.setObjectName("LogUpButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 110, 131, 81))
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Images/3.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 210, 291, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/HP/Downloads/aadarsh/user-login-form.121.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 330, 291, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/HP/Downloads/aadarsh/user-login-form.122.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 30, 391, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/HP/Downloads/lg9 - Copy.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 390, 291, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(QF)

        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 270, 291, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(QF)
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.LogUpButton.setText(_translate("MainWindow", "LOG IN"))
        if self.rto == 0:
            self.LogUpButton.clicked.connect(self.check)
        if self.rto == 1:
            self.LogUpButton.clicked.connect(self.rtologin)

    def check(self):
        import booking_db as t
        t.BookDB().InsertCancleBooking(QDate.currentDate().toString("dd-MM-yyyy"), QTime.currentTime().hour(), "---","---")
        t.BookDB().InsertRTO(QDate.currentDate().toString("dd-MM-yyyy"), QTime.currentTime().hour(), "---", "---")
        self.user = self.textEdit.text()
        self.Pass = self.textEdit_2.text()
        print(self.user)
        print(self.Pass)
        if self.textEdit.text() == "admin" and self.textEdit_2.text() == "admin":
            import adminpy
            self.window = QtWidgets.QMainWindow()

            self.ui = adminpy.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.m.hide()

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
                    self.m.hide()
                    self.window = QtWidgets.QMainWindow()
                    import popup
                    self.ui = popup.Ui_MainWindow()
                    self.ui.setupUi(self.window, "------", "--------","You Are To Late So Please Go UNDERGROUND Section To Pick Up Your Car!!!")
                    self.window.show()
                    # self.ui = succ("------", "--------","You Are To Late So Please Go UNDERGROUND Section To Pick Up Your Car!!!")
                    # self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(), QtCore.QDate.currentDate(), self.ST,
                    #               self.STM, self.ET, self.ETM)


                    '''self.window = QMainWindow(self)
                    self.ui = succ("------", "--------","You Are To Late So Please Go UNDERGROUND Section To Pick Up Your Car!!!")
                    self.ui.show()
                    self.hide()'''
                if no1 != 1:
                    self.m.hide()
                    self.window = QtWidgets.QMainWindow()
                    import popup
                    self.ui = popup.Ui_MainWindow()
                    self.ui.setupUi(self.window, "------", "--------", "No Record Found")
                    self.window.show()

                    # self.ui = succ("------", "--------", "No Record Found")
                    # self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(), QtCore.QDate.currentDate(), self.ST,
                    #               self.STM, self.ET, self.ETM)

                    '''self.window = QMainWindow(self)
                    self.ui = succ("------", "--------", "No Record Found")
                    self.ui.show()
                    self.hide()'''
                if no2 == 1:
                    self.m.hide()
                    self.window = QtWidgets.QMainWindow()
                    import popup
                    self.ui = popup.Ui_MainWindow()
                    self.ui.setupUi(self.window, "------", "--------","Sorry ,You Are To Late Please Again Book Your Slot!!!")
                    self.window.show()
                    # self.ui = succ("------", "--------", "Sorry ,You Are To Late Please Again Book Your Slot!!!")
                    # self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(), QtCore.QDate.currentDate(), self.ST,
                    #               self.STM, self.ET, self.ETM)


                    '''self.window = QMainWindow(self)
                    self.ui = succ("------", "--------", "Sorry ,You Are To Late Please Again Book Your Slot!!!")
                    self.ui.show()
                    self.hide()'''
            if no == 1:
                self.m.hide()
                self.window = QtWidgets.QMainWindow()

                import insertpy
                self.ui = insertpy.Ui_MainWindow()
                self.ui.setupUi(self.window, 0, self.user, self.Pass)
                self.window.show()


                '''self.window = QMainWindow(self)
                self.ui = insert(0, self.user, self.Pass)
                self.ui.show()
                self.hide()'''

    def rtologin(self):
        self.user = self.textEdit.text()
        self.Pass = self.textEdit_2.text()
        db.BookDB().CheckLogIn(self.user, self.Pass)
        no = db.BookDB().CheckRTO(self.user, self.Pass)
        print("no is", no)
        if no == 1:
            self.m.hide()
            self.window = QtWidgets.QMainWindow()
            import insertpy
            self.ui = insertpy.Ui_MainWindow()
            self.ui.setupUi(self.window, 1, self.user, self.Pass)
            self.window.show()
        else:
            self.m.hide()
            self.window = QtWidgets.QMainWindow()
            import popup
            self.ui = popup.Ui_MainWindow()
            self.ui.setupUi(self.window, "------", "--------", "No record found")
            self.window.show()



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

