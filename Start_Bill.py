from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Time_Cal import *
from reg_succ import *
import booking_db as db
import sys
##Note:def __init__(self,cn,sloat,UserEdit,CarEdit,ST,STM,ET,ETM):
class SBill(QMainWindow):
    def __init__(self,sloat,UserEdit,CarEdit,ST,STM,ET,ETM):
       super(SBill, self).__init__()
       self.bill=QLabel(self)
       self.bill.setText("BILL")
       self.bill.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
       self.bill.setGeometry(QRect(225, 17, 101, 41))
       self.cn1=CarEdit
       self.UserName=QLabel(self)
       self.UserName.setText("USER NAME")
       self.UserName.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.UserName.setGeometry(QRect(10, 80, 451, 31))

       self.UserNameEdit=QLabel(self)
       self.UserNameEdit.setText(UserEdit)
       self.UserNameEdit.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.UserNameEdit.setGeometry(QRect(270, 80, 211, 31))
       self.CarNo=QLabel(self)
       self.CarNo.setText("Car No")
       self.CarNo.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.CarNo.setGeometry(QRect(10, 130, 231, 31))
       self.CarNoEdit=QLabel(self)
       self.CarNoEdit.setText(CarEdit)
       self.CarNoEdit.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.CarNoEdit.setGeometry(QRect(270, 130, 171, 31))
       self.STime=QLabel(self)
       self.STime.setText("START TIME")
       self.STime.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.STime.setGeometry(QRect(10, 180, 241, 31))

       self.STimeEdit=QLabel(self)
       self.STimeEdit.setText(str(ST)+":"+str(STM))
       self.STimeEdit.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.STimeEdit.setGeometry(QRect(270, 180, 171, 31))

       self.ETime=QLabel(self)
       self.ETime.setText("END TIME")
       self.ETime.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.ETime.setGeometry(QRect(10, 230, 241, 31))

       self.ETimeEdit=QLabel(self)
       self.ETimeEdit.setText(str(ET)+":"+str(ETM))
       self.ETimeEdit.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.ETimeEdit.setGeometry(QRect(270, 230, 171, 31))
       self.st=ST;self.Smin=STM;self.et=ET;self.etm=ETM
       self.hrs,self.mins = getTime(str(ST)+":"+str(STM),str(ET)+":"+str(ETM))

       self.TotalTime=QLabel(self)
       self.TotalTime.setText("TOTAL TIME")
       self.TotalTime.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.TotalTime.setGeometry(QRect(10, 280, 231, 31))

       self.TotalTimeEdit=QLabel(self)
       self.TotalTimeEdit.setText(self.hrs+":"+self.mins)
       self.TotalTimeEdit.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.TotalTimeEdit.setGeometry(QRect(270, 280, 171, 31))

       self.rs=QLabel(self)
       self.rs.setText("TOTAL RS.")
       self.rs.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.rs.setGeometry(QRect(10, 330, 231, 31))

       self.rs=0.0
       print(self.rs)
       self.rs=self.rs+float(self.hrs)*10.00
       print(self.hrs)
       print(self.rs)
       self.rs=self.rs+float(self.mins)*0.1666666667
       print(self.mins)
       print(self.rs)
       self.rs=round(self.rs)
       print(self.rs)
       self.rsedit=QLabel(self)
       self.rsedit.setText(str(self.rs))
       self.rsedit.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.rsedit.setGeometry(QRect(270, 330, 171, 31))

       self.pay=QPushButton(self)
       self.pay.setText("NEXT")
       self.pay.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.pay.setGeometry(QRect(10, 380, 421, 51))
       self.pay.clicked.connect(self.paid)

       self.dateLabel=QLabel(self)
       self.dateLabel.setText("DATE :")
       self.dateLabel.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.dateLabel.setGeometry(QRect(0,0,171,31))

       self.dateEdit=QLabel(self)
       self.dateEdit.setText(QDate.currentDate().toString("dd-MM-yyyy"))
       self.dateEdit.setFont(QFont("Perpetua Titling MT",15,QFont.Bold))
       self.dateEdit.setGeometry(QRect(175,0,171,31))

       self.sloat1=sloat
       self.setGeometry(0, 0, 700, 500)
       self.show()


    @pyqtSlot()
    def paid(self):
     self.window = QMainWindow(self)
     #InsertPayment(self, date, username, carno, shour, smin, ehour, emin, totaltime, totalrs)
     date=self.dateEdit.text()
     db.BookDB().InsertPayment(date,self.UserNameEdit.text(),self.CarNoEdit.text(),self.st,self.Smin,self.et,self.etm,self.hrs+":"+self.mins,self.rs)
     self.ui = succ(self.cn1,self.sloat1,"PAY YOUR AMOUNT ON COUNTER!!!")
     self.ui.show()
     self.hide()

'''app=QApplication(sys.argv)
Gui=SBill("sloat_6","abc","mh40-8664","10","20","14","19")
sys.exit(app.exec_())'''

