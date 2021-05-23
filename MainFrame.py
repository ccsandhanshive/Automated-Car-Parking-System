from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


import sys
import booking_db as t
class Main(QMainWindow):	#Main Window
    def __init__(self):
        super(Main,self).__init__()
        self.book=QPushButton(self)

        t.BookDB().InsertCancleBooking(QDate.currentDate().toString("dd-MM-yyyy"), QTime.currentTime().hour(), "---", "---")#if  user can be late to park the kar then this is cancle user need to book again
        t.BookDB().InsertRTO(QDate.currentDate().toString("dd-MM-yyyy"), QTime.currentTime().hour(), "---", "---")#if user is not exit car on time then this car can be goes to undergroud
        self.book.setText("BOOKING")
        self.book.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.book.setGeometry(QRect(30, 20, 421, 51))
        self.book.clicked.connect(self.book_in)

        self.login=QPushButton(self)
        self.login.setText("LOGIN")
        self.login.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.login.setGeometry(QRect(30, 90, 421, 61))
        self.login.clicked.connect(self.login_in)

        self.rto=QPushButton(self)
        self.rto.setText("UNDERGROUND")
        self.rto.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.rto.setGeometry(QRect(30, 170, 421, 61))
        self.rto.clicked.connect(self.rto_in)

        self.exit=QPushButton(self)
        self.exit.setText("EXIT")
        self.exit.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.exit.setGeometry(QRect(30, 250, 421, 61))
        self.exit.clicked.connect(self.exit_in)

        self.setGeometry(0,0,500,400)
        self.show()

    @pyqtSlot()
    def book_in(self):			#for book car window
        from Book_page import Book
        self.window = QMainWindow(self)
        self.ui = Book()
        self.ui.show()
        self.hide()




    def login_in(self):				#for login window
        from LogIn import login
        self.window = QMainWindow(self)
        self.ui =login(0)
        self.ui.show()
        self.hide()


    def  rto_in(self):				#for undergroud
        from LogIn import login
        print("RTO LOGIN")
        self.window = QMainWindow(self)
        self.ui = login(1)
        self.ui.show()
        self.hide()


    def exit_in(self):					#for exit
        sys.exit(QApplication(sys.argv).exec_())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    GUI = Main()
    sys.exit(app.exec_())