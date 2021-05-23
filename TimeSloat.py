from PyQt5 import QtSql
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class TimeSloat(QMainWindow):
    def __init__(self):
        super(TimeSloat,self).__init__()


        self.sryLabel1=QLabel(self)
        self.sryLabel2=QLabel(self)
        self.btn=QPushButton(self)
        self.exit=QPushButton(self)
        self.table=QTableView(self)

        QF=QFont("Perpetua Titling MT",16,QFont.Bold)
        self.sryLabel1.setFont(QF)
        self.sryLabel2.setFont(QF)
        self.btn.setFont(QF)
        self.exit.setFont(QF)
        self.table.setFont(QF)

        self.sryLabel1.setText("SRY NO SLOAT AVALABILE FOR YOUR TIME")
        self.sryLabel2.setText("IF YOU CHANGE YOUR TIME THEN ITS POSSIBLE TO ALLOCATE SLOAT")
        self.btn.setText("CLICK HERE TO SHOW TIME AND SLOAT")
        self.exit.setText("EXIT")

        self.sryLabel1.setGeometry(QRect(160, 0, 521, 41))
        self.sryLabel2.setGeometry(QRect(0, 40, 831, 16))
        self.btn.setGeometry(QRect(110, 80, 591, 51))
        self.exit.setGeometry(QRect(110, 150, 591, 51))
        self.table.setGeometry(QRect(110, 220, 581, 331))
        self.resize(861, 600)
        self.show()


    def initializeModel(self,model):
        model.setTable('TimeSloat')
        model.setEditStraregy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0,Qt.Horizontal,"Time")
        model.setHeaderData(1,Qt.Horizontal,"Sloat")

    def createView(self,title,model):
        view=QTableView()
        view.setModel(model)
        view.setModel(model)
        view.setWindowTitle(title)
        return view

    def addrow(self):
        print model.rowCount()
        ret=model.insertRows(model.rowCount(),1)
        print ret

    def findrow(self,i):
        delrow=i.row()

app = QApplication(sys.argv)
GUI = TimeSloat()
model=QtSql.QSqlTableModel()
delrow=-1
TimeSloat.initializeModel(model)
sys.exit(app.exec_())