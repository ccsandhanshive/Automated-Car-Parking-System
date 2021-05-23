from PyQt5.QtCore import *;
from PyQt5.QtWidgets import *;
from PyQt5.QtGui import *;
import booking_db as db
from admin_login import Admin
from insert_car import *
from reg_succ import *
import sys




class login(QMainWindow):				#login window
    def __init__(self,rto):
        super(login,self).__init__()
        t.BookDB().InsertCancleBooking(QDate.currentDate().toString("dd-MM-yyyy"), QTime.currentTime().hour(), "---","---") #if user booked car but does not park there car in system then after 1 hr there booking is cancled
        t.BookDB().InsertRTO(QDate.currentDate().toString("dd-MM-yyyy"), QTime.currentTime().hour(), "---", "---")			#if user cannot receive there car on time then there car park in underground 
        self.tm=timeStart()
        self.tm.chg.connect(self.st)
        self.tm.start()				#thread start
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("login form")
        self.mainlabel = QLabel(self)
        self.mainlabel.setText("Login")
        self.mainlabel.setGeometry(150,50,500,100)
        self.mainlabel.setFont(QFont("mangal_0",20,QFont.Bold))
        self.uloginlabel =QLabel(self)
        self.uloginlabel.setText("user name")
        self.uloginlabel.setGeometry(50,100,500,100)
        self.uloginlabel.setFont(QFont("mangal_0",20,QFont.Medium))
        self.ulogintext =QLineEdit(self)
        self.ulogintext.setText("")
        self.ulogintext.setGeometry(250,140,200,25)
        self.ulogintext.setFont(QFont("mangal_0",10,QFont.Medium))
        self.password = QLabel(self)
        self.password.setText("Password")
        self.password.setGeometry(50,180,200,25)
        self.setFont(QFont("mangal_0",20,QFont.Medium))
        self.passwordtext =QLineEdit(self)
        self.passwordtext.setText("")

        self.passwordtext.setEchoMode(QLineEdit.Password)
        self.passwordtext.setGeometry(250, 180, 200, 25)

        self.setFont(QFont("mangal_0", 20, QFont.Medium))
        self.loginbtn =QPushButton(self)
        self.loginbtn.setText("Login")
        self.loginbtn.setGeometry(50,250,400,50)
        self.loginbtn.setFont(QFont("mangal_0",10,QFont.Bold))
        #self.loginbtn.clicked.connect(self.check)
        print(self.ulogintext.text())
        print(self.passwordtext.text())


        if rto==0:		#if car not in underground then login normally
            self.loginbtn.clicked.connect(self.check)    #connect with check method
        if rto==1:		#if car present in underground then login into underground
            self.loginbtn.clicked.connect(self.rtologin)
        self.timelable =QLabel(self)
        self.timelable.setText("hh:mm:yy")
        self.timelable.setGeometry(260,50,500,50)
        self.timelable.setFont(QFont("mangal_0",20,QFont.Bold))

        self.show()


    @pyqtSlot()
    def check(self):				#for authentication
        self.user=self.ulogintext.text()
        self.Pass=self.passwordtext.text()
        if self.ulogintext.text() == "admin" and self.passwordtext.text() == "admin": #if user is admin or not
            self.window = QMainWindow(self)
            self.ui = Admin()
            self.ui.show()
            self.hide()
        else:												#if user is not admin
            db.BookDB().CheckLogIn(self.user, self.Pass)
            db.BookDB().CheckCancleBook(self.user, self.Pass)
            no = db.BookDB().CheckLogIn(self.user, self.Pass)		#if user is valid then return 1 else return 0
            no2 = db.BookDB().CheckCancleBook(self.user, self.Pass)	#if user booking is cancled then return 1 else 0
            print("no is", no)
            if no != 1:						#if user is not valid
                db.BookDB.CheckRTO(self, self.user, self.Pass)			#check there car present in underground or not
                no1 = db.BookDB.CheckRTO(self, self.user, self.Pass)
                print("no1 is", no1)
                if no1 == 1:									#if car present in underground 
                    self.window = QMainWindow(self)
                    self.ui = succ("------", "--------","You Are To Late So Please Go UNDERGROUND Section To Pick Up Your Car!!!")
                    self.ui.show()
                    self.hide()
                if no1 != 1:									#invalid user
                    self.window = QMainWindow(self)
                    self.ui = succ("------", "--------", "No Record Found")
                    self.ui.show()
                    self.hide()
                if no2 == 1:							#if booking is cancled
                    self.window = QMainWindow(self)
                    self.ui = succ("------", "--------", "Sorry ,You Are To Late Please Again Book Your Slot!!!")
                    self.ui.show()
                    self.hide()
            if no == 1:									#valid user
                self.window = QMainWindow(self)
                self.ui = insert(0, self.user, self.Pass)
                self.ui.show()
                self.hide()




    def rtologin(self):						#underground login
        self.user = self.ulogintext.text()
        self.Pass = self.passwordtext.text()
        db.BookDB().CheckLogIn(self.user, self.Pass)		#check user car is present in underground or not
        no = db.BookDB().CheckRTO(self.user, self.Pass)
        print("no is", no)
        if no == 1:
            self.window = QMainWindow(self)
            self.ui = insert(1,self.user, self.Pass)
            self.ui.show()
            self.hide()







        """user=self.ulogintext.text()
        passw=self.passwordtext.text()
        print(user);print(passw)
        if user=="chetan" and passw=="chetan":
            self.mainlabel.setText("login successs")
            self.panel =QWidget(self)
            self.setCentralWidget(self.panel)
            self.slable=QLabel(self.panel)
            self.slable.setText(" ")
            self.setGeometry(500,500,500,50)
            self.setFont(QFont("mangal_0",20,QFont.Bold))
            self.slable.setText("login success")"""

    @pyqtSlot()
    def st(self):
        self.timelable.setText(QTime.currentTime().toString("hh:mm:ss a"))			#for show current time


class timeStart(QThread):				#thread for continuesly check if user late to park there car or user receive there car on time or not
    chg = pyqtSignal()
    def __init__(self):
        super().__init__()

    def run(self):					#thread run
        while True:
            self.chg.emit()
            self.sleep(1)

'''app=QApplication(sys.argv)
GUI = login(0)
sys.exit(app.exec_())'''