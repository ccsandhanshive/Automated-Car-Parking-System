from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Time_Cal import *
from reg_succ import *
import booking_db as db
import sys

class Cash(QMainWindow):			#if user has get there car before there ending time then it also get cash back max 10 rs or if user late then pay extra payment
    def __init__(self,rto,usernm,carno,endtimehour,endtimemin):
        super(Cash,self).__init__()
        self.cn=carno
        QF=QFont("Perpetua Titling MT",15,QFont.Bold)
        self.CashLabel=QLabel(self)
        if rto==0:
            self.CashLabel.setText("CASHBACK")
        if rto==1:
            self.CashLabel.setText("ETRA PEMENT")
        self.CashLabel.setFont(QF)
        self.CashLabel.setGeometry(QRect(180, 10, 221, 51))

        self.UserName=QLabel(self)
        self.UserName.setText("USER NAME   :")
        self.UserName.setFont(QF)
        self.UserName.setGeometry(QRect(20, 80, 311, 31))

        self.UserNameEdit=QLabel(self)
        self.UserNameEdit.setText(usernm)
        self.UserNameEdit.setFont(QF)
        self.UserNameEdit.setGeometry(QRect(340, 80, 211, 31))

        self.CarNo=QLabel(self)
        self.CarNo.setText("CAR NO.  :")
        self.CarNo.setFont(QF)
        self.CarNo.setGeometry(QRect(20, 130, 301, 31))

        self.CarNoEdit=QLabel(self)
        self.CarNoEdit.setText(carno)
        self.CarNoEdit.setFont(QF)
        self.CarNoEdit.setGeometry(QRect(340, 130, 171, 31))

        self.ETime=QLabel(self)
        self.ETime.setText("END TIME  :")
        self.ETime.setFont(QF)
        self.ETime.setGeometry(QRect(20, 180, 301, 31))

        self.ETimeEdit=QLabel(self)
        self.ETimeEdit.setText(endtimehour+":"+endtimemin)
        self.ETimeEdit.setFont(QF)
        self.ETimeEdit.setGeometry(QRect(340, 180, 161, 31))

        self.CTime=QLabel(self)
        self.CTime.setText("Current Time  :")
        self.CTime.setFont(QF)
        self.CTime.setGeometry(QRect(20, 240, 291, 31))

        self.CTimeEdit=QLabel(self)
        self.CTimeEdit.setText(QTime.currentTime().toString("hh:mm"))
        self.CTimeEdit.setFont(QF)
        self.CTimeEdit.setGeometry(QRect(340, 240, 171, 31))


        self.CTimeEdit.text().split(":")
        self.currentHour=self.CTimeEdit.text()[0]+self.CTimeEdit.text()[1]
        self.currentMin=self.CTimeEdit.text()[3]+self.CTimeEdit.text()[4]
        self.Current=self.currentHour+":"+self.currentMin



        self.hr=endtimehour
        self.min=endtimemin
        self.time=self.hr+":"+self.min
        self.time=endtimehour+":"+endtimemin
        print(self.Current)				#convert in hh:mm fromate
        print(self.time)
        if rto==0:						#if car not in underground 
            getTime(self.Current,self.time)
            self.ReHours,self.ReMin=getTime(self.Current,self.time)
        if rto==1:							#if car in underground 
            getTime(self.time, self.Current)
            self.ReHours, self.ReMin =getTime(self.time, self.Current)
        print(self.ReHours)
        print(self.ReMin)
        print(self.currentHour)
        print(self.currentMin)
        self.crs=0.0
        if rto==0:
            try:
                self.crs=float(self.crs)+float(self.ReHours)*10.00				#add cashback 10 rs per hour
                self.crs=float(self.crs)+float(self.ReMin)*0.1666666667			#add cashback 0.167 rs per min
            except:
                print("Exeception")
        if rto==1:
            try:
                self.crs=float(self.crs)+float(self.ReHours)*15.50				#add extra payment as 15.50 rs per hr 
                self.crs=float(self.crs)+float(self.ReMin)*0.2583333333			#add extra payment as 0.259 rs per min
            except:
                print("Exeception")



        self.crs=round(self.crs)
        self.RTime=QLabel(self)
        if rto==0:
            self.RTime.setText("Remaining Time :")
        if rto==1:
            self.RTime.setText("Extra Time  :")
        self.RTime.setFont(QF)
        self.RTime.setGeometry(QRect(20, 310, 311, 31))

        self.RTimeEdit=QLabel(self)
        self.RTimeEdit.setText(self.ReHours+":"+self.ReMin)
        self.RTimeEdit.setFont(QF)
        self.RTimeEdit.setGeometry(QRect(340, 310, 171, 31))

        self.CashbackRs=QLabel(self)
        if rto==0:
            if self.crs>10.00:
                self.crs=10.00									#Max cashback 10 rs only
            self.CashbackRs.setText("CASHBACK RS.")
        if rto==1:
            self.CashbackRs.setText("Extra Rs.  :")
        self.CashbackRs.setFont(QF)
        self.CashbackRs.setGeometry(QRect(10, 370, 321, 31))

        self.CashbackRsEdit=QLabel(self)
        self.CashbackRsEdit.setText(str(self.crs))
        self.CashbackRsEdit.setFont(QF)
        self.CashbackRsEdit.setGeometry(QRect(340, 370, 171, 31))

        self.btn=QPushButton(self)
        if rto==0:
            self.btn.setText("Collect amount from counter!!")		#if you get cashback collect amount from counter
        if rto==1:
            self.btn.setText("NEXT")
        self.btn.setFont(QF)
        self.btn.setGeometry(QRect(10, 420, 491, 61))
        self.btn.clicked.connect(self.ex)
        self.un=usernm
        self.cn=carno
        self.endtime= endtimehour + ":" + endtimemin


        self.setGeometry(0,0,700,600)
        self.show()


    @pyqtSlot()
    def ex(self):									#car exit
        db.BookDB().InsertCashBack(self.un,self.cn,self.endtime,self.currentHour + ":" + self.currentMin, self.ReHours + ":" + self.ReMin, self.crs)
        print("data sucessfully insert in cashback")
        db.BookDB().updateRTO(self.cn,self.ReHours+":"+self.ReMin,self.crs)
        print("All Records Deleted Succesfully!!")
        self.window = QMainWindow(self)
        import reg_succ as s
        self.ui = s.succ("-------------", "--------", "Car exit Success!!!!!!!!!!")
        self.ui.show()
        self.hide()



'''app=QApplication(sys.argv)
GUI=Cash(0,"abc","mh30-2762","18","20")
sys.exit(app.exec_())'''