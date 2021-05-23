# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_pageui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime

import slotpy


class Ui_MainWindow(QtWidgets.QMainWindow):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(766, 501)
        QF = QtGui.QFont("Perpetua Titling MT", 14)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 110, 151, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 180, 151, 41))
        self.label_2.setObjectName("label_2")
        self.UserEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserEdit.setFont(QF)
        self.UserEdit.setGeometry(QtCore.QRect(470, 120, 291, 41))
        self.UserEdit.setObjectName("UserEdit")
        self.CarEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CarEdit.setGeometry(QtCore.QRect(470, 180, 291, 41))
        self.CarEdit.setFont(QF)
        self.CarEdit.setObjectName("CarEdit")
        self.BookButton = QtWidgets.QPushButton(self.centralwidget)
        self.BookButton.setGeometry(QtCore.QRect(360, 390, 181, 41))
        self.BookButton.setMaximumSize(QtCore.QSize(181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BookButton.setFont(font)
        self.BookButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"color: rgb(255, 255, 255);")
        self.BookButton.setObjectName("BookButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 240, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 290, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 251, 341))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./Images/2.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.STime = QtWidgets.QComboBox(self.centralwidget)
        self.STime.setFont(QF)
        self.STime.setGeometry(QtCore.QRect(470, 240, 81, 31))
        self.STime.setObjectName("STime")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STime.addItem("")
        self.STimem = QtWidgets.QTimeEdit(self.centralwidget)
        self.STimem.setFont(QF)
        self.STimem.setGeometry(QtCore.QRect(580, 240, 91, 31))
        self.STimem.setObjectName("STimem")
        self.STimeAM = QtWidgets.QComboBox(self.centralwidget)
        self.STimeAM.setFont(QF)
        self.STimeAM.setGeometry(QtCore.QRect(700, 240, 61, 31))
        self.STimeAM.setObjectName("STimeAM")
        self.STimeAM.addItem("")
        self.STimeAM.addItem("")
        self.ETime = QtWidgets.QComboBox(self.centralwidget)
        self.ETime.setFont(QF)
        self.ETime.setGeometry(QtCore.QRect(470, 290, 81, 31))
        self.ETime.setObjectName("ETime")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETime.addItem("")
        self.ETimem = QtWidgets.QTimeEdit(self.centralwidget)
        self.ETimem.setGeometry(QtCore.QRect(580, 290, 91, 31))
        self.ETimem.setObjectName("ETimem")
        self.ETimeAM = QtWidgets.QComboBox(self.centralwidget)
        self.ETimeAM.setFont(QF)
        self.ETimeAM.setGeometry(QtCore.QRect(700, 290, 61, 31))
        self.ETimeAM.setObjectName("ETimeAM")
        self.ETimeAM.addItem("")
        self.ETimeAM.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 330, 101, 21))
        self.label_8.setStyleSheet("color: rgb(239, 79, 0);")
        self.label_8.setObjectName("label_8")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setFont(QF)
        self.dateEdit.setGeometry(QtCore.QRect(470, 330, 291, 41))
        self.dateEdit.setObjectName("dateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ETimem.setFont(QF)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">New User Name</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Car Number</span></p></body></html>"))
        self.BookButton.setText(_translate("MainWindow", "Book Slot"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Start Time</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">End Time</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#005500;\">Booking Here</span></p></body></html>"))
        self.STime.setItemText(0, _translate("MainWindow", "11"))
        self.STime.setItemText(1, _translate("MainWindow", "12"))
        self.STime.setItemText(2, _translate("MainWindow", "01"))
        self.STime.setItemText(3, _translate("MainWindow", "02"))
        self.STime.setItemText(4, _translate("MainWindow", "03"))
        self.STime.setItemText(5, _translate("MainWindow", "04"))
        self.STime.setItemText(6, _translate("MainWindow", "05"))
        self.STime.setItemText(7, _translate("MainWindow", "06"))
        self.STime.setItemText(8, _translate("MainWindow", "07"))
        self.STime.setItemText(9, _translate("MainWindow", "08"))
        self.STime.setItemText(10, _translate("MainWindow", "09"))
        self.STime.setItemText(11, _translate("MainWindow", "10"))
        self.STimeAM.setItemText(0, _translate("MainWindow", "AM"))
        self.STimeAM.setItemText(1, _translate("MainWindow", "PM"))
        self.ETime.setItemText(0, _translate("MainWindow", "11"))
        self.ETime.setItemText(1, _translate("MainWindow", "12"))
        self.ETime.setItemText(2, _translate("MainWindow", "01"))
        self.ETime.setItemText(3, _translate("MainWindow", "02"))
        self.ETime.setItemText(4, _translate("MainWindow", "03"))
        self.ETime.setItemText(5, _translate("MainWindow", "04"))
        self.ETime.setItemText(6, _translate("MainWindow", "05"))
        self.ETime.setItemText(7, _translate("MainWindow", "06"))
        self.ETime.setItemText(8, _translate("MainWindow", "07"))
        self.ETime.setItemText(9, _translate("MainWindow", "08"))
        self.ETime.setItemText(10, _translate("MainWindow", "09"))
        self.ETime.setItemText(11, _translate("MainWindow", "10"))
        self.ETimeAM.setItemText(0, _translate("MainWindow", "AM"))
        self.ETimeAM.setItemText(1, _translate("MainWindow", "PM"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Date</span></p></body></html>"))
        self.BookButton.clicked.connect(self.insert)
        self.c = QDate.currentDate().toString()
        print(self.c)
        self.STime.currentIndexChanged.connect(self.hrChanged)
        self.STimeAM.currentIndexChanged.connect(self.AMChenge)
        self.ETime.currentIndexChanged.connect(self.AMChange)
        self.ETimem.timeChanged.connect(self.AMChg)
        self.M=MainWindow
        self.STimem.setDisplayFormat("mm")
        self.ETimem.setDisplayFormat("mm")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarPopup()
        self.dateEdit.setMinimumDate(QDate.currentDate())

    def insert(self):
        self.ST = self.STime.currentText()
        self.ET = self.ETime.currentText()
        self.STM = self.STimem.text()
        self.ETM = self.ETimem.text()
        print(self.ST)
        print(self.ET)
        print(self.STimeAM.currentText())
        print(self.ETimeAM.currentText())
        if self.STimeAM.currentText() == "PM":
            self.ST = int(self.ST) + 12
            print("ST PM:"+str(self.ST))
        if self.ETimeAM.currentText() == "PM":
            self.ET = int(self.ET) + 12
            print("ET PM:"+str(self.ET))
        if self.ETime.currentText() == "12" and self.ETimeAM.currentText() == "AM":
            print("12:AM")

            self.ET=int(self.ET)+12
            print("12:AM"+str(self.ET))
        print(self.STime.currentText())
        print(self.STimeAM.currentText())
        if self.ETime.currentText() == "12" and self.ETimeAM.currentText() == "PM":
            print("12:PM")

            self.ET=int(self.ET)-12
            print("12:PM"+str(self.ET))

        if self.STime.currentText() == "12" and self.STimeAM.currentText() == "AM":

            self.ST=int(self.ST)+12
            print("12:AM ST"+str(self.ST))
        if self.STime.currentText() == "12" and self.STimeAM.currentText() == "PM":

            self.ST=int(self.ST)-12
            print("12:PM ST"+str(self.ST))




        print(self.ST)
        print(self.ET)
        import booking_db as db
        a = db.BookDB().insertData(self.UserEdit.text(), self.CarEdit.text(), self.ST, self.STM, self.ET, self.ETM)
        if a == -1:
            self.window = QtWidgets.QMainWindow()
            import popup
            self.ui = popup.Ui_MainWindow()
            self.ui.setupUi(self.window, "------", "--------", "Duplicate Car Entry")
            self.window.show()

            '''self.window = QtWidgets.QMainWindow(self)
            self.ui = succ("------", "------", "--------","Duplicate Car Entry"))
            self.ui.show()'''
        else:
            self.ok()

    def ok(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = slotpy.Ui_MainWindow()
        self.ui.setupUi(self.window, self.UserEdit.text(), self.CarEdit.text(),self.dateEdit.text(), self.ST,
                        self.STM, self.ET, self.ETM)

        self.window.show()
        self.M.hide()


        '''self.window = QtWidgets.QMainWindow(self)
        print(self.Date.acceptDrops())
        self.ui=Sloat(self.UserEdit.text(),self.CarEdit.text(),self.Date.text(),self.ST,self.STM,self.ET,self.ETM)
        #self.ui.__init__(self.CarEdit.text(),self.Date.text(),self.STime.currentText(),self.ETime.currentText())
        self.ui.show()
        self.hide()'''

    def hrChanged(self):

        hr = int(self.STime.currentText())
        am = str(self.STimeAM.currentText())
        while hr <= 12:
            if hr <= 9:
                self.ETime.addItem("0{}".format(hr))
            else:
                self.ETime.addItem("{}".format(hr))
            hr += 1

        if am == "PM":
            self.ETime.clear()
            while hr <= 12:
                if hr <= 9:
                    self.ETime.addItem("0{}".format(hr))
                else:
                    self.ETime.addItem("{}".format(hr))
                hr += 1

    def AMChenge(self):

        pm = str(self.STimeAM.currentText())

        if pm == "PM":
            self.ETimeAM.clear()
            self.ETimeAM.addItem("PM")

    def AMChange(self):
        em = int(self.ETime.currentText())
        sm = int(self.STime.currentText())
        print("amchg")
        print(em)
        print(sm)
        if em <= sm:
            if em == sm:
                smm = int(self.STimem.text())
                emm = int(self.ETimem.text())
                if smm > emm:
                    print(em)
                    print(sm)
                    self.ETimeAM.clear()
                    self.ETimeAM.addItem("PM")
                else:
                    self.ETimeAM.clear()
                    self.ETimeAM.addItem("AM")
                    self.ETimeAM.addItem("PM")
            else:
                self.ETimeAM.clear()
                self.ETimeAM.addItem("PM")
        if em > sm:
            self.ETimeAM.clear()
            self.ETimeAM.addItem("AM")
            self.ETimeAM.addItem("PM")

    def AMChg(self):
        smm = int(self.STimem.text())
        emm = int(self.ETimem.text())
        if smm > emm:
            self.ETimeAM.clear()
            self.ETimeAM.addItem("PM")
        else:
            self.ETimeAM.clear()
            self.ETimeAM.addItem("AM")
            self.ETimeAM.addItem("PM")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
