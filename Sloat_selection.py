from PyQt5.QtCore import *;
from PyQt5.QtGui import *;
from PyQt5.QtWidgets import *;
import booking_db as t
from Registration_form import *
from Start_Bill import *
from sry1 import Ui_MainWindow
import sys
class Sloat(QMainWindow):
    def __init__(self,user,CarNo,Date,STime,STimeM,ETime,ETimeM): 
        super(Sloat,self).__init__()
        self.setGeometry(500,500,900,500)
        self.un=user
        self.t=CheckThered()
        self.t.check.connect(self.AutoCheck)
        self.t.start()
        self.s1=QPushButton(self)
        self.s2=QPushButton(self)
        self.s3=QPushButton(self)
        self.s4 = QPushButton(self)

        self.s5 = QPushButton(self)
        self.s6 = QPushButton(self)
        self.s7 = QPushButton(self)
        self.s8 = QPushButton(self)
        self.s1.setText("SLOT 1")
        self.s2.setText("SLOT 2")
        self.s3.setText("SLOT 3")
        self.s4.setText("SLOT 4")
        self.s5.setText("SLOT 5")
        self.s6.setText("SLOT 6")
        self.s7.setText("SLOT 7")
        self.s8.setText("SLOT 8")
        self.s1.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.s2.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.s3.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.s4.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.s5.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.s6.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.s7.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.s8.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.s1.setGeometry(QRect(30, 10, 161, 91))
        self.s2.setGeometry(QRect(220, 10, 161, 91))
        self.s3.setGeometry(QRect(410, 10, 161, 91))
        self.s4.setGeometry(QRect(590, 10, 161, 91))
        self.s5.setGeometry(QRect(30, 120, 161, 91))
        self.s6.setGeometry(QRect(220, 120, 161, 91))
        self.s7.setGeometry(QRect(410, 120, 161, 91))
        self.s8.setGeometry(QRect(590, 120, 161, 91))
        self.select = QPushButton(self)
        self.select.setText("No Slot available Click Here!!")
        self.select.setFont(QFont("Perpetua Titling MT",30,QFont.Bold))
        self.select.setGeometry(QRect(32, 267, 721, 51))
        self.select.setVisible(False)
        print(CarNo,Date,int(STime),int(STimeM),int(ETime),int(ETimeM))
        self.cn=CarNo
        self.dt=Date
        self.S=int(STime)
        self.SM=int(STimeM)
        self.e=int(ETime)
        self.em=int(ETimeM)
        #self.s8.setStyleSheet("background-color: red")
        print(self.s1.styleSheet())
        #if self.s1.styleSheet()=='red'
        self.s1.clicked.connect(self.s1F)
        self.s2.clicked.connect(self.s2F)
        self.s3.clicked.connect(self.s3F)
        self.s4.clicked.connect(self.s4F)
        self.s5.clicked.connect(self.s5F)
        self.s6.clicked.connect(self.s6F)
        self.s7.clicked.connect(self.s7F)
        self.s8.clicked.connect(self.s8F)
        self.select.clicked.connect(self.jump)
        #self.s8.setStyleSheet("red")

        self.show()





    @pyqtSlot()
    def AutoCheck(self):				#Check all slot if slot already booked at that time this slot is invisible otherwise visible and ready to book
        t.BookDB().InsertCancleBooking(self.dt, QTime.currentTime().hour(), "---", "---")
        t.BookDB().InsertRTO(self.dt,QTime.currentTime().hour(),"---","---")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_1")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_1")
        if a != 0:
            self.s1.setStyleSheet("background-color: red")
            self.s1.hide()
        print("Sloat 1")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_2")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_2")
        if a != 0:
            self.s2.setStyleSheet("background-color: red")
            self.s2.hide()
        print("Sloat 2")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_3")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_3")
        if a != 0:
            self.s3.setStyleSheet("background-color: red")
            self.s3.hide()
        print("Sloat 3")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_4")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_4")
        if a != 0:
            self.s4.setStyleSheet("background-color: red")
            self.s4.hide()
        print("Sloat 4")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_5")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_5")
        if a != 0:
            self.s5.setStyleSheet("background-color: red")
            self.s5.hide()
        print("Sloat 5")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_6")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_6")
        if a != 0:
            self.s6.setStyleSheet("background-color: red")
            self.s6.hide()
        print("Sloat 6")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_7")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_7")
        if a != 0:
            self.s7.setStyleSheet("background-color: red")
            self.s7.hide()
        print("Sloat 7")

        t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_8")
        a = t.BookDB().CheckSloat(self.dt, self.S,self.SM, self.e,self.em, "sloat_8")
        if a != 0:
            self.s8.setStyleSheet("background-color: red")
            self.s8.hide()
        print("Sloat 8")

        if self.s1.isVisible() == False and self.s2.isVisible() == False and self.s3.isVisible() == False and self.s4.isVisible() == False and self.s5.isVisible() == False and self.s6.isVisible() == False and self.s7.isVisible() == False and self.s8.isVisible() == False:
            self.select.setVisible(True)
            '''self.panal=QWidget(self)
            self.panal.setGeometry(500,500,900,500)

            self.panal.sryLabel = QLabel(self.panal)
            self.panal.sryLabel.setText("SRY No Sloat Available For You!!!")
            self.panal.sryLabel.setFont(QFont("Perpetua Titling MT", 20, QFont.Bold))
            self.panal.sryLabel.setGeometry(QRect(30, 10, 1000, 50))
            self.panal.showSloat = QPushButton(self.panal)
            self.panal.showSloat.setText("Click here to show Time and Sloat!!!")
            self.panal.showSloat.setFont(QFont("Perpetua Titling MT", 20, QFont.Bold))
            self.panal.showSloat.setGeometry(QRect(32, 267, 721, 101))
            # self.showSloat.clicked.connect(self.SloatTime)
            self.panal.show()'''

    def s1F(self):			#book slot 1
        t.BookDB().insertSloat(self.cn, self.dt, self.S,self.SM, self.e,self.em,"sloat_1")
        self.s1.setStyleSheet("background-color: red")

        print("Sloat 1")
        self.Log_up("sloat_1")

    def s2F(self):			#book slot 2
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_2")
        self.s2.setStyleSheet("background-color: red")
        print("Sloat 2")
        self.Log_up("sloat_2")

    def s3F(self):
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_3")
        self.s3.setStyleSheet("background-color: red")
        print("Sloat 3")
        self.Log_up("sloat_3")

    def s4F(self):
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_4")
        self.s4.setStyleSheet("background-color: red")
        print("Sloat 4")
        self.Log_up("sloat_4")

    def s5F(self):
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_5")
        self.s5.setStyleSheet("background-color: red")
        print("Sloat 5")
        self.Log_up("sloat_5")

    def s6F(self):
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_6")
        self.s6.setStyleSheet("background-color: red")
        print("Sloat 6")
        self.Log_up("sloat_6")

    def s7F(self):
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_7")
        self.s7.setStyleSheet("background-color: red")
        print("Sloat 7")
        self.Log_up("sloat_7")

    def s8F(self):
        t.BookDB().insertSloat(self.cn, self.dt, self.S, self.SM, self.e, self.em,"sloat_8")
        self.s8.setStyleSheet("background-color: red")
        print("Sloat 8")
        self.Log_up("sloat_8")

    def Log_up(self,sloat):
        self.window1 = QMainWindow(self)
        self.ui1 = SBill(sloat,self.un, self.cn, self.S, self.SM, self.e, self.em)
        self.ui1.show()
        self.hide()
    def jump(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.hide()













class CheckThered(QThread):
    check= pyqtSignal()
    def run(self):
        while True:
            self.check.emit()
            QThread.sleep(1)

'''app = QApplication(sys.argv)
GUI = Sloat("raj","mh90-4567","23-09-2018","12","00","24","00")
sys.exit(app.exec_())'''

