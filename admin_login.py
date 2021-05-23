from PyQt5.QtCore import *
from PyQt5.QtGui import *;
from PyQt5.QtWidgets import *;
import booking_db as db
import sys
from delete import Ui_MainWindow as delete
class Admin(QMainWindow):
    def __init__(self):
        super(Admin,self).__init__()
        QF=QFont("Perpetua Titling MT",16,QFont.Bold)	#set font name ,size and title
        self.adLable = QLabel(self)						#create a label
        self.adLable.setText("ADMIN LOGIN")				#set lable name
        self.adLable.setFont(QF)						#set font
        self.adLable.setGeometry(QRect(260, 20, 281, 31))	#QRect(x1,y1,x2,y2)

        self.gbtn=QPushButton(self)
        self.gbtn.setText("CURRENT DATA ANALYSIS VIA GRAPH")
        self.gbtn.setFont(QF)
        self.gbtn.setGeometry(QRect(60, 80, 711, 61))
        self.gbtn.clicked.connect(self.draw)			#linking with draw method

        self.tbtn=QPushButton(self)
        self.tbtn.setText("CURRENT DATA ANALYSIS AND DELETE VIA TABLE")
        self.tbtn.setFont(QF)
        self.tbtn.setGeometry(QRect(60, 160, 711, 61))
        self.tbtn.clicked.connect(self.analysis)

        self.ogbtn=QPushButton(self)
        self.ogbtn.setText("History DATA ANLYSIS VIA GRAPH")
        self.ogbtn.setFont(QF)
        self.ogbtn.setGeometry(QRect(60, 240, 711, 61))
        self.ogbtn.clicked.connect(self.draw1)

        self.otbtn=QPushButton(self)
        self.otbtn.setText("History DATA ANALYSIS VIA TABLE")
        self.otbtn.setFont(QF)
        self.otbtn.setGeometry(QRect(60, 320, 711, 61))
        self.otbtn.clicked.connect(self.analysis1)


        self.exit=QPushButton(self)
        self.exit.setText("EXIT")
        self.exit.setFont(QF)
        self.exit.setGeometry(QRect(60, 400, 711, 51))
        self.exit.clicked.connect(self.exit_)




        self.setGeometry(0,0,798, 520)
        self.show()
    def draw(self):											#for draw pie chart of current table
        import matplotlib.pyplot as plt
        booking,canclebooking,exitcar,parkcar,rto_payment=db.BookDB().CheckBooking(0)
        labels = 'booking', 'canclebooking', 'exitcar', 'parkcar','rto'
        sizes = [booking,canclebooking,exitcar,parkcar,rto_payment]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
        explode = (0, 0, 0, 0,0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()

    def draw1(self):									#for draw pie chart of history table
        import matplotlib.pyplot as plt
        booking,canclebooking,exitcar,parkcar,rto_payment=db.BookDB().CheckBooking(1)
        labels = 'booking', 'canclebooking', 'exitcar', 'parkcar','rto'
        sizes = [booking,canclebooking,exitcar,parkcar,rto_payment]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
        explode = (0, 0, 0, 0,0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()






    def analysis(self):									#retrive data from verias current tables at admin site 
        self.window=QMainWindow()
        self.ui=delete()								#for delete retrive and delete data 
        self.ui.setupUi(self.window,0)
        self.window.show()

    def analysis1(self):								#retrive data from verias history table at admin site but cannot delete
        self.window=QMainWindow()
        self.ui=delete()
        self.ui.setupUi(self.window,1)
        self.window.show()




    def exit_(self):									#back to previous window
        self.window = QMainWindow(self)
        import MainFrame as m
        self.ui = m.Main()
        self.ui.show()
        self.hide()
        #sys.exit(QApplication(sys.argv).exec_())







'''app = QApplication(sys.argv)
GUI = Admin()
sys.exit(app.exec_())'''






