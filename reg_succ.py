from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys




class succ(QMainWindow):
    def __init__(self,cn,sloat,msg):
        super(succ,self).__init__()
        self.setGeometry(0,0,800,250)
        self.label=QLabel(self)
        self.label.setText(msg)
        self.label.setGeometry(QRect(10, 10, 741, 71))
        self.label.setFont(QFont("Perpetua Titling MT",12,QFont.Bold))
        self.btn=QPushButton(self)
        self.btn.setText("OK")
        self.btn.setGeometry(QRect(210, 100, 93, 28))
        self.btn.setFont(QFont("Perpetua Titling MT",12,QFont.Bold))
        self.m = msg

        if self.m == "PAY YOUR AMOUNT ON COUNTER!!!":
            self.btn.clicked.connect(self.exit1)
        else:
            if self.m=="PassWord Missmatch!!!!!!" or self.m=="Duplicate Car Entry":
                self.btn.clicked.connect(self.exit3)
            else:
                self.btn.clicked.connect(self.exit2)


        self.cn1=cn
        self.sloat1=sloat



        self.show()


    @pyqtSlot()
    def exit1(self):
        self.window = QMainWindow(self)
        import Registration_form as r
        self.ui= r.reg(self.cn1,self.sloat1)
        self.ui.show()
        self.hide()


    def exit2(self):

        self.window=QMainWindow(self)
        import MainFrame as m
        self.ui =m.Main()
        self.ui.show()
        self.hide()


    def exit3(self):
        self.hide()











'''app = QApplication(sys.argv)
GUI = succ("mh40","sloat_1","Congo! Registration Successful!!")
sys.exit(app.exec_())'''