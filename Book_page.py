from datetime import date

from PyQt5.QtCore import *
from PyQt5.QtGui import *;
from PyQt5.QtWidgets import *;
import sys
import booking_db as db
from Sloat_selection import *
from Start_Bill import *
class Book(QMainWindow):
    def __init__(self):
        super(Book,self).__init__()
        self.MainLabel=QLabel(self)
        self.setGeometry(0,0,750,800)
        self.MainLabel.setText("BOOKING HERE")
        self.MainLabel.setGeometry(QRect(230, 30, 311, 41))
        self.MainLabel.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.UserLabel=QLabel(self)
        self.UserLabel.setText("USER NAME")
        self.UserLabel.setGeometry(QRect(100, 100, 181, 31))
        self.UserLabel.setFont(QFont("Perpetua Titling MT",18))
        self.UserEdit=QLineEdit(self)
        self.UserEdit.setText("")
        self.UserEdit.setGeometry(QRect(290, 100, 441, 31))
        self.UserEdit.setFont(QFont("Perpetua Titling MT",17))
        self.CarLabel=QLabel(self)
        self.CarLabel.setText("Car No.")
        self.CarLabel.setFont(QFont("Perpetua Titling MT",18))
        self.CarLabel.setGeometry(QRect(100, 170, 161, 31))
        self.CarEdit=QLineEdit(self)
        self.CarEdit.setFont(QFont("Perpetua Titling MT",18))
        self.CarEdit.setGeometry(QRect(290, 170, 441, 31))
        self.TimeLabel=QLabel(self)
        self.TimeLabel.setText("TIME")
        self.TimeLabel.setFont(QFont("Perpetua Titling MT",18))
        self.TimeLabel.setGeometry(QRect(100, 240, 161, 31))
        self.STime = QComboBox(self)
        self.STime.setGeometry(QRect(290, 240, 57, 31))
        self.STime.setFont(QFont("Perpetua Titling MT", 12))
        #self.STime.setDisplayFormat("hh")
        self.STimem=QTimeEdit(self)
        self.STimem.setGeometry(QRect(350, 240, 57, 31))
        self.STimem.setFont(QFont("Perpetua Titling MT", 17))
        self.STimem.setDisplayFormat("mm")

        self.STime.addItem("12")
        self.STime.addItem("01")
        self.STime.addItem("02")
        self.STime.addItem("03")
        self.STime.addItem("04")
        self.STime.addItem("05")
        self.STime.addItem("06")
        self.STime.addItem("07")
        self.STime.addItem("08")
        self.STime.addItem("09")
        self.STime.addItem("10")
        self.STime.addItem("11")
        self.STimeAM = QComboBox(self)
        self.STimeAM.setFont(QFont("Perpetua Titling MT", 17))
        self.STimeAM.setGeometry(QRect(410, 240, 71, 31))
        self.STimeAM.addItem("AM")
        self.STimeAM.addItem("PM")
        self.ETime = QComboBox(self)
        self.ETime.setFont(QFont("Perpetua Titling MT", 12))
        self.to=QLabel(self)
        self.to.setText("TO")
        self.to.setFont(QFont("Perpetua Titling MT", 18))
        self.to.setGeometry(QRect(500, 240, 41, 31))
        self.ETime.setGeometry(QRect(550, 240, 57, 31))
        #self.ETime.setDisplayFormat("HH")
        self.ETimem=QTimeEdit(self)
        self.ETimem.setGeometry(QRect(610, 240, 57, 31))
        self.ETimem.setFont(QFont("Perpetua Titling MT", 17))
        self.ETimem.setDisplayFormat("mm")
        self.ETime.addItem("12")
        self.ETime.addItem("01")
        self.ETime.addItem("02")
        self.ETime.addItem("03")
        self.ETime.addItem("04")
        self.ETime.addItem("05")
        self.ETime.addItem("06")
        self.ETime.addItem("07")
        self.ETime.addItem("08")
        self.ETime.addItem("09")
        self.ETime.addItem("10")
        self.ETime.addItem("11")

        self.ETimeAM = QComboBox(self)
        self.ETimeAM.setGeometry(QRect(670, 240, 71, 31))
        self.ETimeAM.setFont(QFont("Perpetua Titling MT", 18))
        self.ETimeAM.addItem("AM")
        self.ETimeAM.addItem("PM")
        self.BookButton=QPushButton(self)
        self.BookButton.setText("BOOKING")
        self.BookButton.setFont(QFont("Perpetua Titling MT", 18,QFont.Bold))
        self.BookButton.setGeometry(QRect(100, 520, 641, 51))
        self.BookButton.clicked.connect(self.insert)
        self.c=QDate.currentDate().toString()
        print(self.c)


        self.Date=QDateEdit(self)

        self.STime.currentIndexChanged.connect(self.hrChanged)
        self.STimeAM.currentIndexChanged.connect(self.AMChenge)
        self.ETime.currentIndexChanged.connect(self.AMChange)
        self.ETimem.timeChanged.connect(self.AMChg)
        self.Date.setDate(QDate.currentDate())
        self.Date.setGeometry(QRect(300, 320, 241, 51))
        self.Date.setCalendarPopup(True)
        self.Date.calendarPopup()
        self.Date.setMinimumDate(QDate.currentDate())
        #self.Date.setDate(self)
        #self.Date.setDateRange(min)
        self.Date.setFont(QFont("Perpetua Titling MT", 18))
        self.DateLabel=QLabel(self)
        self.DateLabel.setText("DATE")
        self.DateLabel.setFont(QFont("Perpetua Titling MT", 18))
        self.DateLabel.setGeometry(QRect(100,300,100,35))


        self.show()





    @pyqtSlot()
    def insert(self):
        self.ST = self.STime.currentText()	#get starting time HH
        self.ET = self.ETime.currentText()	#get ending time HH
        self.STM=self.STimem.text()			#get starting minite
        self.ETM=self.ETimem.text()			#get ending minite
        print(self.ST)
        print(self.ET)
        print(self.STimeAM.currentText() )
        print(self.ETimeAM.currentText() )
        if self.ETime.currentText()=="12" and self.ETimeAM.currentText()=="AM":	
            print("12:AM")
            self.ET=int(self.ET)+12				#add 12 in 12 means time is 24
        elif self.ETime.currentText()=="12" and self.ETimeAM.currentText()=="PM":
            print("12:PM")
            self.ET=int(self.ET)				#not need to time 
        elif self.STime.currentText()=="12" and self.STimeAM.currentText()=="AM":
            self.ST=int(self.ST)+12				#add 12 in 12 means time is 24
        elif self.ETime.currentText()=="12" and self.ETimeAM.currentText()=="PM":
            self.ST=int(self.ST)				#not need to add anything
        else:
            print("other")
            if self.STimeAM.currentText() == "PM":
                self.ST = int(self.ST) + 12			#if PM add 12 in given time

            if self.ETimeAM.currentText() == "PM":
                self.ET = int(self.ET) + 12			#if PM add 12 in given time


        print(self.ST)
        print(self.ET)
        a=db.BookDB().insertData(self.UserEdit.text(), self.CarEdit.text(), self.ST,self.STM,self.ET,self.ETM)	#add data into booking table
        if a==-1:
            self.window = QMainWindow(self)
            self.ui = succ("------", "--------","Duplicate Car Entry")		#if carno already present into table then display duplicate car entry
            self.ui.show()
        else:
            self.ok()														#else jump to ok method



    def ok(self):												#Display slote booking
        self.window = QMainWindow(self)
        print(self.Date.acceptDrops())
        self.ui=Sloat(self.UserEdit.text(),self.CarEdit.text(),self.Date.text(),self.ST,self.STM,self.ET,self.ETM)	#display slotes for booking
        #self.ui.__init__(self.CarEdit.text(),self.Date.text(),self.STime.currentText(),self.ETime.currentText())
        self.ui.show()
        self.hide()

    def hrChanged(self):										#for hr dropdown option

        hr = int(self.STime.currentText())
        am=str(self.STimeAM.currentText())
        while hr <= 12:							#for show 01 to 12 in dropdown 
            if hr <= 9:
                self.ETime.addItem("0{}".format(hr))
            else:
                self.ETime.addItem("{}".format(hr))
            hr += 1									#hr++

        if am=="PM":
            self.ETime.clear()
            while hr <= 12:							#for show 01 to 12 in dropdown
                if hr <= 9:
                    self.ETime.addItem("0{}".format(hr))
                else:
                    self.ETime.addItem("{}".format(hr))
                hr += 1



    def AMChenge(self):								#For AM PM dropdown option

        pm=str(self.STimeAM.currentText())

        if pm=="PM":
            self.ETimeAM.clear()
            self.ETimeAM.addItem("PM")


    def AMChange(self):						#for AM PM dropdown 
        em=int(self.ETime.currentText())
        sm=int(self.STime.currentText())
        print("amchg")
        print(em)
        print(sm)
        if em<=sm:
            if em==sm:
                smm=int(self.STimem.text())
                emm=int(self.ETimem.text())
                if smm>emm:
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
        if em>sm:
            self.ETimeAM.clear()
            self.ETimeAM.addItem("AM")
            self.ETimeAM.addItem("PM")



    def AMChg(self):							#For AM PM dropdown option
        smm = int(self.STimem.text())
        emm = int(self.ETimem.text())
        if smm > emm:
            self.ETimeAM.clear()
            self.ETimeAM.addItem("PM")
        else:
            self.ETimeAM.clear()
            self.ETimeAM.addItem("AM")
            self.ETimeAM.addItem("PM")










'''app = QApplication(sys.argv)
GUI = Book()
sys.exit(app.exec_())'''
