from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import reg_succ as c
import booking_db as db
import sys




class reg(QMainWindow):
    def __init__(self,CarNo,SloatNo):
        super(reg,self).__init__()
        self.Mainlabel=QLabel(self)
        self.cr=CarNo
        self.sn=SloatNo
        self.Mainlabel.setText("Slot Booked Successfully!")
        self.Mainlabel.setFont(QFont("Perpetua Titling MT",20,QFont.Bold))
        self.Mainlabel.setGeometry(QRect(160, 10, 550, 51))

        self.CreateLabel=QLabel(self)
        self.CreateLabel.setText("Create Your Login")
        self.CreateLabel.setFont(QFont("Perpetua Titling MT",18,QFont.Bold))
        self.CreateLabel.setGeometry(QRect(260, 70, 381, 41))

        self.UserLabel=QLabel(self)
        self.UserLabel.setText("User Name")
        self.UserLabel.setFont(QFont("Perpetua Titling MT",15))
        self.UserLabel.setGeometry(QRect(50, 150, 151, 31))

        self.UserEdit=QLineEdit(self)
        self.UserEdit.setFont(QFont("Perpetua Titling MT",15))
        self.UserEdit.setGeometry(QRect(330, 150, 451, 41))

        self.PassLabel=QLabel(self)
        self.PassLabel.setText("PassWord")
        self.PassLabel.setFont(QFont("Perpetua Titling MT",15))
        self.PassLabel.setGeometry(QRect(50, 220, 121, 31))

        self.PassEdit=QLineEdit(self)
        self.PassEdit.setFont(QFont("Perpetua Titling MT",15))
        self.PassEdit.setGeometry(QRect(330, 220, 451, 41))
        self.PassEdit.setEchoMode(QLineEdit.Password)

        self.RePassLabel=QLabel(self)
        self.RePassLabel.setText("Re-Enter Password")
        self.RePassLabel.setFont(QFont("Perpetua Titling MT",15))
        self.RePassLabel.setGeometry(QRect(50, 300, 431, 21))


        self.RePassEdit=QLineEdit(self)
        self.RePassEdit.setFont(QFont("Perpetua Titling MT",15))
        self.RePassEdit.setGeometry(QRect(330, 290, 451, 41))
        self.RePassEdit.setEchoMode(QLineEdit.Password)

        self.LogUpButton=QPushButton(self)
        self.LogUpButton.setText("LOG UP")
        self.LogUpButton.setFont(QFont("Perpetua Titling MT",22,QFont.Bold))
        self.LogUpButton.setGeometry(QRect(50, 360, 734, 51))
        self.LogUpButton.clicked.connect(self.LogUp)

        self.setGeometry(500,500,800,500)
        self.show()



    @pyqtSlot()
    def LogUp(self):
        self.user=self.UserEdit.text()
        self.passw=self.PassEdit.text()
        self.Rpass=self.RePassEdit.text()
        if self.passw==self.Rpass:
            self.window = QMainWindow(self)
            db.BookDB().InsertLogUp(self.user, self.passw, self.cr, self.sn)
            self.ui =c.succ("-------------","-----------","Congo! Registration Successful!!")
            #self.ui = r.succ(self.cr,self.sn,"Congo!!!!!!!!! Registration Successful!!!!!!!!!!!1")
            self.ui.show()
            self.hide()
        else:
            self.window = QMainWindow(self)
            self.ui = c.succ("-------------", "-----------", "PassWord And RePassword are  Missmatch!!!!!!")
            self.ui.show()






'''app = QApplication(sys.argv)
GUI = reg("mh40","sloat_1")
sys.exit(app.exec_())'''
