# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regsucess.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):				#popup window
    def setupUi(self, MainWindow,cn,sloat,msg):  #previous window,car no, slot no,msg
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 187)
        self.m = msg
        self.cn1 = cn
        self.sloat1 = sloat
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1091, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 90, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
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
        self.label.setText(_translate("MainWindow", self.m))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        if self.m == "PAY YOUR AMOUNT ON COUNTER!!!":
            self.pushButton.clicked.connect(self.exit1)
        else:
            if self.m=="PassWord Missmatch!!!!!!" or self.m=="Duplicate Car Entry" or self.m=="Please try another username!":
                self.pushButton.clicked.connect(self.exit3)
            else:
                self.pushButton.clicked.connect(self.exit2)

    def exit1(self):#display logup window
        self.m.hide()
        self.window = QtWidgets.QMainWindow()
        import loguppy
        self.ui = loguppy.Ui_MainWindow()
        self.ui.setupUi(self.window,self.cn1,self.sloat1)  #previous window,car no,slot no
        self.window.show()
        '''self.window = QtWidgets.QMainWindow()
        import Registration_form as r
        self.ui= r.reg(self.cn1,self.sloat1)
        self.ui.show()'''



    def exit2(self):		#for main window

        self.m.hide()
        self.window=QtWidgets.QMainWindow()
        import mainpy
        self.ui = mainpy.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        '''self.window = QtWidgets.QMainWindow()
        import popup
        self.ui = popup.Ui_MainWindow()
        self.ui.setupUi(self.window,cn,sloat,msg)
        self.window.show()'''



        '''import MainFrame as m
        self.ui =m.Main()
        self.ui.show()'''



    def exit3(self):		#simple hide

        self.m.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,"mh40","sloat_1","PassWord Missmatch!!!!!!" )
    MainWindow.show()
    sys.exit(app.exec_())

