# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import booking_db as db

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 728)
        import booking_db as t
        t.BookDB().InsertCancleBooking(QtCore.QDate.currentDate().toString("dd-MM-yyyy"), QtCore.QTime.currentTime().hour(), "---", "---")
        t.BookDB().InsertRTO(QtCore.QDate.currentDate().toString("dd-MM-yyyy"), QtCore.QTime.currentTime().hour(), "---", "---")
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 0, 281, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 26pt \"MS Shell Dlg 2\";\n"
"")
        self.label.setObjectName("label")
        self.bktable = QtWidgets.QPushButton(self.centralwidget)
        self.bktable.setGeometry(QtCore.QRect(130, 480, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bktable.setFont(font)
        self.bktable.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.bktable.setObjectName("bktable")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(570, 610, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.17 rgba(255, 0, 0, 255), stop:0.18 rgba(255, 255, 255, 255), stop:0.210212 rgba(255, 255, 255, 255), stop:0.220212 rgba(0, 16, 255, 255), stop:0.279897 rgba(0, 16, 255, 255), stop:0.289897 rgba(255, 255, 255, 255), stop:0.32 rgba(255, 255, 255, 255), stop:0.33 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);")
        self.exit.setObjectName("exit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 151, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./Images/adminLogin.png"))
        self.label_2.setObjectName("label_2")
        self.bktable_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bktable_2.setGeometry(QtCore.QRect(130, 400, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bktable_2.setFont(font)
        self.bktable_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.bktable_2.setObjectName("bktable_2")
        self.bktable_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bktable_3.setGeometry(QtCore.QRect(130, 320, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bktable_3.setFont(font)
        self.bktable_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.bktable_3.setObjectName("bktable_3")
        self.bktable_4 = QtWidgets.QPushButton(self.centralwidget)
        self.bktable_4.setGeometry(QtCore.QRect(130, 240, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bktable_4.setFont(font)
        self.bktable_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.bktable_4.setObjectName("bktable_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 26))
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
        self.label.setText(_translate("MainWindow", "ADMIN LOGIN"))
        self.bktable.setText(_translate("MainWindow", "BACKUP DATA ANALYSIS VIA TABLE"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.bktable_2.setText(_translate("MainWindow", "BACKUP DATA ANALYSIS VIA GRAPH"))
        self.bktable_3.setText(_translate("MainWindow", "SHOW CURRENT STATUS VIA TABLE"))
        self.bktable_4.setText(_translate("MainWindow", "SHOW CURRENT STATUS VIA GRAPH"))
        self.bktable_4.clicked.connect(self.draw)
        self.bktable_3.clicked.connect(self.analysis)
        self.bktable_2.clicked.connect(self.draw1)
        self.bktable.clicked.connect(self.analysis1)
        self.exit.clicked.connect(self.exit_)


    def draw(self):
        import matplotlib.pyplot as plt
        booking,canclebooking,exitcar,parkcar,rto_payment=db.BookDB().CheckBooking(0)
        labels = 'booking', 'canclebooking', 'exitcar', 'parkcar','rto'
        sizes = [booking,canclebooking,exitcar,parkcar,rto_payment]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
        explode = (0, 0, 0, 0,0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()

    def draw1(self):
        import matplotlib.pyplot as plt
        booking,canclebooking,exitcar,parkcar,rto_payment=db.BookDB().CheckBooking(1)
        labels = 'booking', 'canclebooking', 'exitcar', 'parkcar','rto'
        sizes = [booking,canclebooking,exitcar,parkcar,rto_payment]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
        explode = (0, 0, 0, 0,0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()






    def analysis(self):

        self.window = QtWidgets.QMainWindow()
        import showpy
        self.ui = showpy.Ui_MainWindow()
        self.ui.setupUi(self.window,0)
        self.window.show()




        '''self.window=QtWidgets.QMainWindow()

        self.ui=delete()
        self.ui.setupUi(self.window,0)
        self.window.show()'''

    def analysis1(self):

        self.window = QtWidgets.QMainWindow()
        import showpy
        self.ui = showpy.Ui_MainWindow()
        self.ui.setupUi(self.window, 1)
        self.window.show()
        '''self.window=QtWidgets.QMainWindow()
        self.ui=delete()
        self.ui.setupUi(self.window,1)
        self.window.show()'''




    def exit_(self):
        self.m.hide()
        self.window = QtWidgets.QMainWindow()
        import mainpy
        self.ui = mainpy.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

