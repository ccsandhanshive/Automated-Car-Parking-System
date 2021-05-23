# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logupui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):					#Log up window
    def setupUi(self, MainWindow,CarNo,SloatNo):
        MainWindow.setObjectName("MainWindow")
        QF = QtGui.QFont("Perpetua Titling MT", 14)
        self.cr=CarNo
        self.sn=SloatNo
        MainWindow.resize(497, 486)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(10, 10, 201, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.MainLabel.setFont(font)
        self.MainLabel.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 85, 0);")
        self.MainLabel.setObjectName("MainLabel")
        self.UserLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserLabel.setGeometry(QtCore.QRect(210, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.UserLabel.setFont(font)
        self.UserLabel.setStyleSheet("\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.UserLabel.setObjectName("UserLabel")

        self.UserEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserEdit.setGeometry(QtCore.QRect(210, 150, 231, 31))
        self.UserEdit.setObjectName("UserEdit")
        self.UserEdit.setFont(QF)
        self.PassLabel = QtWidgets.QLabel(self.centralwidget)
        self.PassLabel.setGeometry(QtCore.QRect(210, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PassLabel.setFont(font)
        self.PassLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.PassLabel.setObjectName("PassLabel")
        self.LogUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogUpButton.setGeometry(QtCore.QRect(210, 340, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.LogUpButton.setFont(font)
        self.LogUpButton.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.LogUpButton.setObjectName("LogUpButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 401, 41))
        self.label.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"\n"
"text-decoration: underline;\n"
"color: rgb(85, 85, 0);")
        self.label.setObjectName("label")
        self.PassEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PassEdit.setGeometry(QtCore.QRect(210, 220, 231, 31))
        self.PassEdit.setFont(QF)
        self.PassEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PassEdit.setObjectName("PassEdit")
        self.PassLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.PassLabel_2.setGeometry(QtCore.QRect(210, 260, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PassLabel_2.setFont(font)
        self.PassLabel_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.PassLabel_2.setObjectName("PassLabel_2")
        self.RePassEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RePassEdit.setFont(QF)
        self.RePassEdit.setGeometry(QtCore.QRect(210, 290, 231, 31))
        self.RePassEdit.setObjectName("RePassEdit")
        self.RePassEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 191, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./Images/5.png"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 26))
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
        self.MainLabel.setText(_translate("MainWindow", "SLOT BOOKED SUCCESSFULLY"))
        self.UserLabel.setText(_translate("MainWindow", "USER-NAME"))
        self.PassLabel.setText(_translate("MainWindow", "PASSWORD"))
        self.LogUpButton.setText(_translate("MainWindow", "LOG UP"))
        self.label.setText(_translate("MainWindow", "*CREATE YOUR LOGIN*"))
        self.PassLabel_2.setText(_translate("MainWindow", "RE-ENTER PASSWORD"))
        self.LogUpButton.clicked.connect(self.LogUp)
    def LogUp(self):				#log up 
        import reg_succ as c
        self.user=self.UserEdit.text()
        self.passw=self.PassEdit.text()
        self.Rpass=self.RePassEdit.text()
        if self.passw==self.Rpass:


            import booking_db as db
            a=db.BookDB().InsertLogUp(self.user, self.passw, self.cr, self.sn)	#Check password and reEnterd password is same or not
            self.m.hide()
            self.window = QtWidgets.QMainWindow()

            import popup
            self.ui = popup.Ui_MainWindow()
            if a==0:			#if password not missmatch
                self.ui.setupUi(self.window,"-------------","-----------","Congo! Registration Successful!!")			#if registration is completed
            else:
                self.ui.setupUi(self.window, "-------------", "-----------", "Please try another username!")			#if username already present
                self.m.show()
            self.window.show()
            #self.ui =c.succ("-------------","-----------","Congo! Registration Successful!!")
            #self.ui = r.succ(self.cr,self.sn,"Congo!!!!!!!!! Registration Successful!!!!!!!!!!!1")


        else:	#if password missmatch

            self.window = QtWidgets.QMainWindow()
            import popup
            self.ui = popup.Ui_MainWindow()
            self.ui.setupUi(self.window,"-------------", "-----------", "PassWord Missmatch!!!!!!")
            self.window.show()


            #self.ui = c.succ("-------------", "-----------", "PassWord And RePassword are  Missmatch!!!!!!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,"mh908","sloat_1")
    MainWindow.show()
    sys.exit(app.exec_())

