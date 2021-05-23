from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import booking_db as db
from reg_succ import *
import booking_db as t
from cash_Back import *


class insert(QMainWindow):								#for park car in automated car parking system
    def __init__(self,rto,user,passw):
        super(insert,self).__init__()


        self.rto=rto
        if rto==0:						#if car is not present in underground
            db.BookDB().CheckCar(user,passw)					#authentication
            UserName,CarNo,TimeStart,TimeStartMin,TimeEnd,TimeEndMin=db.BookDB().CheckCar(user,passw)   #return username, carno, start hr, startmin, end hr , end min.
        if rto==1:						#if car present in underground 
            db.BookDB().LoginRTO(user, passw)					#
            UserName, CarNo, TimeStart, TimeStartMin, TimeEnd, TimeEndMin = db.BookDB().LoginRTO(user, passw)

        self.un=UserName
        self.cn=CarNo
        self.ts=TimeStart
        self.tsm=TimeStartMin
        self.te=TimeEnd
        self.tem=TimeEndMin
        print("username: {0}     car_no: {1}    time start : {2}   time end : {3}  ".format(self.un,self.cn,self.ts+":"+self.tsm,self.te+":"+self.tem))
        self.LoginLabel=QLabel(self)
        self.setGeometry(0,0,700,600)
        self.LoginLabel.setText("LOGIN SUCCESSFULLY!!")
        self.LoginLabel.setGeometry(QRect(80, 20, 380, 41))
        self.LoginLabel.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))

        self.UserName=QLabel(self)
        self.UserName.setText("USER NAME  :")
        self.UserName.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.UserName.setGeometry(QRect(50, 90, 201, 31))

        self.UserLabel=QLabel(self)
        self.UserLabel.setText(UserName)
        self.UserLabel.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.UserLabel.setGeometry(QRect(320, 90, 361, 31))

        self.CarNo=QLabel(self)
        self.CarNo.setText("CAR NO.       :")
        self.CarNo.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.CarNo.setGeometry(QRect(50, 150, 191, 31))

        self.CarLabel=QLabel(self)
        self.CarLabel.setText(CarNo)
        self.CarLabel.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.CarLabel.setGeometry(QRect(320, 150, 371, 31))

        self.TimeStartLabel=QLabel(self)
        self.TimeStartLabel.setText("TIME START :")
        self.TimeStartLabel.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.TimeStartLabel.setGeometry(QRect(50, 210, 190, 41))

        self.TimeStartShow=QLabel(self)
        self.TimeStartShow.setText(self.ts+":"+self.tsm)
        self.TimeStartShow.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.TimeStartShow.setGeometry(QRect(320, 210, 371, 31))

        self.TimeEndLabel=QLabel(self)
        self.TimeEndLabel.setText("End Time")
        self.TimeEndLabel.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.TimeEndLabel.setGeometry(QRect(50, 270, 261, 31))

        self.TimeEndShow=QLabel(self)
        self.TimeEndShow.setText(self.te+":"+self.tem)
        self.TimeEndShow.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.TimeEndShow.setGeometry(QRect(320, 270, 401, 31))

        self.CurrentTime=QLabel(self)
        self.CurrentTime.setText("CURRENT TIME   :")
        self.CurrentTime.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.CurrentTime.setGeometry(QRect(50, 330, 301, 31))

        self.ShowCuuentTime=QLabel(self)
        self.ShowCuuentTime.setText(QTime.currentTime().toString("hh:mm"))
        self.ShowCuuentTime.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.ShowCuuentTime.setGeometry(QRect(320, 330, 371, 31))
        self.cnt=db.BookDB().CheckCarPark(self.cn)			#check  is car already park or not
        self.cnt1=db.BookDB().CheckCarExit(self.cn)			#check  is car already receive or not
        if rto!=1:					#if car not in underground
            if self.cnt==0:								#if car is not park
                self.ParkButton=QPushButton(self)
                self.ParkButton.setText("PARK THE CAR")
                self.ParkButton.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
                self.ParkButton.setGeometry(QRect(50, 390, 451, 61))
                self.ParkButton.clicked.connect(self.Park)			#linking to park method
        if self.cnt1==0 and self.cnt!=0 or rto==1:				#if car is already receive and its also not park or car is in underground then
            self.ExitButton=QPushButton(self)
            self.ExitButton.setText("Exit The Car")
            self.ExitButton.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
            self.ExitButton.setGeometry(QRect(50, 470, 451, 61))
            self.ExitButton.clicked.connect(self.Exit)				#connect car exit method
            self.show()


    @pyqtSlot()
    def Park(self):						#for insert data into ParkCar table
        db.BookDB().ParkCarInsert(self.un,self.cn,self.ts,self.tsm,self.te,self.tem)
        print("data park insert")
        self.window = QMainWindow(self)
        self.ui = succ("-------------","--------","car Park Successfully!!!!!!!!!!")
        self.hide()

    def Exit(self):						#insert data in exitcar table
        c=str(QDate.currentDate().toString("dd-MM-yyyy"))		#get current time
        print(c)
        db.BookDB().ParkCarExit(c,self.un,self.cn,self.ts,self.tsm,self.te,self.tem)

        print("data exit insert")
        db.BookDB().DeleteAllRecords(self.cn)
        self.window = QMainWindow(self)
        if self.rto==0: #if car not in underground
            self.ui = Cash(0,self.un,self.cn,self.te,self.tem)			#get cashback
        if self.rto==1:			#if car in underground 
            self.ui = Cash(1, self.un, self.cn, self.te, self.tem)			#pay extra payment
            db.BookDB().DeleteRto(self.cn)				#remove car from rto 
        self.ui.show()
        self.hide()




'''app = QApplication(sys.argv)
GUI = insert(1,"aakash","aakash")
sys.exit(app.exec_())'''
