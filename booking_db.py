import mysql.connector
from PyQt5.QtCore import QTime

import Time_Cal as tc


class BookDB():											
    def insertData(self,var,var1,var2,var3,var4,var5):	#starting hr,starting min,ending hr,ending min,car no, slot no in booking table
        dbconnect=mysql.connector.connect(host="localhost",user="root",password="",port="3306",database="sampledb")
        dbcurcor=dbconnect.cursor()
        Insert="insert into booking values('{0}','{1}','{2}','{3}','{4}','{5}');".format(var,var1,var2,var3,var4,var5)
        #print("'{0}','{1}','{2}','{3}'".format(var,var1,var2,var3))
        print(Insert)
        try:
            dbcurcor.execute(Insert)

        except:
            return -1
        print("hii")
        dbconnect.commit()
        dbcurcor.close()
        dbconnect.close()
        return 0

    def insertSloat(self,var,var1,var2,var3,var4,var5,sloat):					#(carno, date, start hr,end hr, slot,) insert data into perticuler slot
        dbconnect1 = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sloat_info")
        dbcurcor1 = dbconnect1.cursor()
        Select = "select Start_hour,Start_min,End_hour,End_min from {4} where CarNo='{0}' and Date='{1}' and Start_hour>{2} and End_hour<{3} ".format(var,var1,var2-1,var4+1,sloat)
        #print("'{0}','{1}','{2}','{3}'".format(var, var1, var2, var3))
        print(Select)
        dbcurcor1.execute(Select)
        cnt1=0
        for row in dbcurcor1:
            if row[0]==var2:
                if row[1]>=var3:
                    if row[2]==var4:
                        if row[3]<=var5:
                            cnt1=cnt1+1





        if cnt1==0:
            dbconnect1 = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sloat_info")
            dbcurcor1 = dbconnect1.cursor()
            Insert="insert into {6} values('{0}','{1}','{2}','{3}','{4}','{5}')".format(var,var1,var2,var3,var4,var5,sloat)
            print(Insert)
            dbcurcor1.execute(Insert)
            dbconnect1.commit()
            dbcurcor1.close()
            dbconnect1.close()
            print("data insert")

        print("hii")
        try:
            dbconnect1.commit()
        except:
            print("already committed")
        print(dbcurcor1.rowcount)
        dbcurcor1.close()
        dbconnect1.close()

    def CheckSloat(self, var1, var2, sm,var3,em,sloat):
        dbconnect1a = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sloat_info")
        dbcurcor1a = dbconnect1a.cursor()
        Select = "select Start_hour,Start_min,End_hour,End_min from {3} where  Date='{0}' and Start_hour>{1} and End_hour<{2}".format(var1, var2 - 1,var3 + 1, sloat)
        print("'{0}','{1}','{2}'".format(var1, var2, var3))
        print(Select)
        dbcurcor1a.execute(Select)
        cnt1 = 0
        for row in dbcurcor1a:
            if row[0] == var2:
                if row[1] >= sm:
                    if row[2] == var3:
                        if row[3] <= em:
                            cnt1 = cnt1 + 1
                    else:
                        cnt1=cnt1+1
            else:
                cnt1=cnt1+1
            print("count",cnt1)

        return cnt1

    def InsertLogUp(self,user,passw,carno,sloatno):
        dbconnect1 = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcor1 = dbconnect1.cursor()
        Insert = "insert into logup values('{0}','{1}','{2}','{3}')".format(user,passw,carno,sloatno)
        print(Insert)
        try:
            dbcurcor1.execute(Insert)
        except:
            return -1
        dbconnect1.commit()
        dbcurcor1.close()
        dbconnect1.close()
        print("data insert")
        return 0


    def CheckLogIn(self,user,Pass):
        dbconnect1 = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcor1 = dbconnect1.cursor()
        Select = "select b.TimeStart,b.TimeStartMin from logup l,booking b where l.UserName='{0}' and l.PassWord='{1}' and b.TimeStart<'{2}' and l.CarNo=b.CarNo".format(user,Pass,int(QTime.currentTime().hour())+1)

        print(Select)
        cnt0=0
        dbcurcor1.execute(Select)
        for row in dbcurcor1:
            if int(row[0])==int(QTime.currentTime().hour()):
                if int(row[1])<=int(QTime.currentTime().minute()):
                    cnt0=cnt0+1

            else:
                cnt0=cnt0+1
        return cnt0
        dbconnect1.commit()
        dbcurcor1.close()
        dbconnect1.close()


    def CheckCar(self,user,Pass):
        dbconnect11 = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcor11 = dbconnect11.cursor()
        select="SELECT b.UserName,l.CarNo,b.TimeStart,b.TimeStartMin,b.TimeEnd ,b.TimeEndMin from Booking b,logup l where l.CarNo=b.CarNo and l.UserName='{0}' and  l.PassWord='{1}'".format(user,Pass)
        UserName=""
        CarNo=""
        TimeStart=""
        TimeStartMin=""
        TimeEnd=""
        TimeEndMin=""

        print(select)
        dbcurcor11.execute(select)

        for row in dbcurcor11:
            UserName=row[0]
            CarNo=row[1]
            TimeStart=row[2]
            TimeStartMin=row[3]
            TimeEnd=row[4]
            TimeEndMin=row[5]
            #break

        dbconnect11.commit()
        dbcurcor11.close()
        dbconnect11.close()
        return UserName,CarNo,TimeStart,TimeStartMin,TimeEnd,TimeEndMin


    def ParkCarInsert(self,user,carno,timestart,timestartmin,timeend,timeendmin):
        dbconnect111 = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="sampledb")
        dbcurcor111 = dbconnect111.cursor()
        insert="insert into parkcar values('{}','{}','{}','{}','{}','{}')".format(user,carno,timestart,timestartmin,timeend,timestartmin)
        dbcurcor111.execute(insert)
        dbconnect111.commit()
        dbcurcor111.close()
        dbconnect111.close()

    def ParkCarExit(self,date, user, carno, timestart,timestartmin, timeend,timeendmin):
        dbconnect111 = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcor111 = dbconnect111.cursor()
        insert = "insert into exitcar values('{}','{}','{}','{}','{}','{}','{}')".format(date,user, carno, timestart,timestartmin, timeend,timeendmin)
        dbcurcor111.execute(insert)
        dbconnect111.commit()
        dbcurcor111.close()
        dbconnect111.close()

    def DeleteAllRecords(self,CarNo):
        dbconnect111 = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="sampledb")
        dbcurcor111 = dbconnect111.cursor()
        DeteteBooking="delete from booking where CarNo='{}' ".format(CarNo)
        Detetelogup="delete from logup where CarNo='{}'".format(CarNo)
        DeleteCanclebooking="delete from canclebooking where CarNo='{}'".format(CarNo)
        DeleteCarExit="delete from exitcar where CarNo='{}'".format(CarNo)
        Deteteparkcar="delete  from parkcar where CarNo='{}'".format(CarNo)
        DeletePayment="delete from payment where CarNo='{}'".format(CarNo)
        DeleteSloat_1="delete  from sloat_info.sloat_1 where CarNo='{}'".format(CarNo)
        DeleteSloat_2="delete  from sloat_info.sloat_2 where CarNo='{}'".format(CarNo)
        DeleteSloat_3="delete  from sloat_info.sloat_3 where CarNo='{}'".format(CarNo)
        DeleteSloat_4="delete  from sloat_info.sloat_4 where CarNo='{}'".format(CarNo)
        DeleteSloat_5="delete  from sloat_info.sloat_5 where CarNo='{}'".format(CarNo)
        DeleteSloat_6="delete  from sloat_info.sloat_6 where CarNo='{}'".format(CarNo)
        DeleteSloat_7="delete  from sloat_info.sloat_7 where CarNo='{}'".format(CarNo)
        DeleteSloat_8="delete  from sloat_info.sloat_8 where CarNo='{}'".format(CarNo)
        dbcurcor111.execute(DeletePayment)
        dbcurcor111.execute(DeleteCanclebooking)
        dbcurcor111.execute(DeleteCarExit)
        dbcurcor111.execute(DeteteBooking)
        print("DeleteBooking")
        #dbconnect111.commit()
        dbcurcor111.execute(Detetelogup)
        print("Deletelogup")
        #dbconnect111.commit()
        dbcurcor111.execute(Deteteparkcar)
        print("Deleteparkcar")
        #dbconnect111.commit()
        dbcurcor111.execute(DeleteSloat_1)
        print("Deletesloat_1")
        #dbconnect111.commit()
        dbcurcor111.execute(DeleteSloat_2)
        print("Deletesloat_2")
        #dbconnect111.commit()
        dbcurcor111.execute(DeleteSloat_3)
        print("Deletesloat_3")
        #dbconnect111.commit()
        dbcurcor111.execute(DeleteSloat_4)
        print("Deletesloat_4")
        #dbconnect111.commit()
        dbcurcor111.execute(DeleteSloat_5)
        print("Deletesloat_5")
        #dbconnect111.commit()
        dbcurcor111.execute(DeleteSloat_6)
        print("Deletesloat_6")
        #dbconnect111.commit()
        dbcurcor111.execute(DeleteSloat_7)
        print("Deletesloat_7")
        #dbconnect111.commit()
        dbcurcor111.execute(DeleteSloat_8)
        print("Deletesloat_8")
        dbconnect111.commit()
        dbcurcor111.close()
        dbconnect111.close()


    def InsertPayment(self,date,username,carno,shour,smin,ehour,emin,totaltime,totalrs):
        dbconnectPay= mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="sampledb")
        dbcurcorPay= dbconnectPay.cursor()
        insertPay="insert into payment values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(date,username,carno,shour,smin,ehour,emin,totaltime,totalrs)
        dbcurcorPay.execute(insertPay)
        dbconnectPay.commit()
        dbcurcorPay.close()
        dbconnectPay.close()


    def InsertRTO(self,date,currenthour,ExTime,Exrs):
        dbconnectrto = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcorrto = dbconnectrto.cursor()
        select = "select l.UserName,l.PassWord,l.CarNo,b.TimeStart,b.TimeStartMin,b.TimeEnd,b.TimeEndMin from booking b,logup l,parkcar p where b.CarNo=l.CarNo and l.CarNo=p.CarNo and b.TimeEnd<'{}'".format(currenthour+1)
        print(select)
        dbcurcorrto.execute(select)
        result = dbcurcorrto.fetchall()
        for row in result:
            print("result")
            print(row[5])
            print("    ",currenthour)
            if int(row[5]) == int(currenthour):
                print(row[6])

                if int(row[6]) <int(QTime.currentTime().minute()):
                    print(row[0] + "  " + row[1] + "  " + row[2] + "   " + row[3] + "   " + row[4] + "   " + row[5] + "   " + row[6])
                    insert = "insert into rto_payment values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(date, row[0], row[1], row[2], row[3], row[4], row[5], row[6], ExTime, Exrs)
                    dbcurcorrto.execute(insert)
                    dbconnectrto.commit()
                    print(row)

                    delete = "DELETE FROM logup WHERE CarNo='{}'".format(row[2])
                    print(delete)
                    dbcurcorrto.execute(delete)
                    dbconnectrto.commit()
                    CarNo = row[2]
                    DeteteBooking = "delete from booking where CarNo='{}' ".format(CarNo)
                    Detetelogup = "delete from logup where CarNo='{}'".format(CarNo)
                    Deteteparkcar = "delete  from parkcar where CarNo='{}'".format(CarNo)
                    DeleteSloat_1 = "delete  from sloat_info.sloat_1 where CarNo='{}'".format(CarNo)
                    DeleteSloat_2 = "delete  from sloat_info.sloat_2 where CarNo='{}'".format(CarNo)
                    DeleteSloat_3 = "delete  from sloat_info.sloat_3 where CarNo='{}'".format(CarNo)
                    DeleteSloat_4 = "delete  from sloat_info.sloat_4 where CarNo='{}'".format(CarNo)
                    DeleteSloat_5 = "delete  from sloat_info.sloat_5 where CarNo='{}'".format(CarNo)
                    DeleteSloat_6 = "delete  from sloat_info.sloat_6 where CarNo='{}'".format(CarNo)
                    DeleteSloat_7 = "delete  from sloat_info.sloat_7 where CarNo='{}'".format(CarNo)
                    DeleteSloat_8 = "delete  from sloat_info.sloat_8 where CarNo='{}'".format(CarNo)
                    dbcurcorrto.execute(DeteteBooking)
                    print("DeleteBooking")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(Detetelogup)
                    print("Deletelogup")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(Deteteparkcar)
                    print("Deleteparkcar")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(DeleteSloat_1)
                    print("Deletesloat_1")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(DeleteSloat_2)
                    print("Deletesloat_2")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(DeleteSloat_3)
                    print("Deletesloat_3")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(DeleteSloat_4)
                    print("Deletesloat_4")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(DeleteSloat_5)
                    print("Deletesloat_5")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(DeleteSloat_6)
                    print("Deletesloat_6")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(DeleteSloat_7)
                    print("Deletesloat_7")
                    dbconnectrto.commit()
                    dbcurcorrto.execute(DeleteSloat_8)
                    print("Deletesloat_8")
                    dbconnectrto.commit()
                    #self.DeleteAllRecords(CarNo)

        dbcurcorrto.close()
        dbconnectrto.close()

    def CheckRTO(self,user,Pass1):
        dbconnectRT = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcorRT = dbconnectRT.cursor()
        select = "SELECT * from rto_payment where UserName='{}' and  PassWord='{}'".format(user,Pass1)
        print(select)
        dbcurcorRT.execute(select)

        for row in dbcurcorRT:
            print("count")
        return dbcurcorRT.rowcount
        dbconnectRT.commit()
        dbcurcorRT.close()
        dbconnectRT.close()



    def LoginRTO(self,user,Pass):
        dbconnectR = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcorR = dbconnectR.cursor()
        select = "SELECT username,carno,start_hour,start_min,end_hour,end_min from rto_payment where UserName='{}' and  PassWord='{}'".format(user,Pass)
        UserName = ""
        CarNo = ""
        TimeStart = ""
        TimeStartMin = ""
        TimeEnd = ""
        TimeEndMin = ""

        print(select)
        dbcurcorR.execute(select)

        for row in dbcurcorR:
            UserName = row[0]
            CarNo = row[1]
            TimeStart = row[2]
            TimeStartMin = row[3]
            TimeEnd = row[4]
            TimeEndMin = row[5]
            break

        dbconnectR.commit()
        dbcurcorR.close()
        dbconnectR.close()
        return UserName, CarNo, TimeStart, TimeStartMin, TimeEnd, TimeEndMin

    def updateRTO(self,carno,ExTime,ExRs):
        dbconnectrto = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcorrto = dbconnectrto.cursor()
        update = "update rto_payment set extra_time='{}' where carno='{}' ".format(ExTime,carno)
        dbcurcorrto.execute(update)
        update = "update rto_payment set extra_rs='{}' where carno='{}' ".format(ExRs, carno)
        dbcurcorrto.execute(update)
        dbconnectrto.commit()
        dbcurcorrto.close()
        dbconnectrto.close()

    def DeleteRto(self,cn):
        dbconnectrto1 = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="sampledb")
        dbcurcorrto1 = dbconnectrto1.cursor()
        update = "delete from rto_payment where CarNo='{}' ".format(cn)
        dbcurcorrto1.execute(update)

        dbconnectrto1.commit()
        dbcurcorrto1.close()
        dbconnectrto1.close()

    def CheckCarPark(self,carno):
        dbconnectPark = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcorPark = dbconnectPark.cursor()
        check="select * from parkcar where CarNo='{}'".format(carno)
        dbcurcorPark.execute(check)

        result=dbcurcorPark.fetchall()
        for i in result:
            print(i)
        return dbcurcorPark.rowcount
        dbcurcorPark.close()
        dbconnectPark.close()

    def CheckCarExit(self,carno):
        dbconnectExit = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcorExit = dbconnectExit.cursor()
        check="select * from exitcar where CarNo='{}'".format(carno)
        dbcurcorExit.execute(check)

        result=dbcurcorExit.fetchall()
        for i in result:
            print(i)
        return dbcurcorExit.rowcount
        dbcurcorExit.close()
        dbconnectExit.close()


    def InsertCancleBooking(self,date,currenthour,ExTime,Exrs):
        dbconnectrto = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcorrto = dbconnectrto.cursor()
        select = "select l.UserName,l.PassWord,l.CarNo,b.TimeStart,b.TimeStartMin,b.TimeEnd,b.TimeEndMin from booking b,logup l where b.CarNo=l.CarNo and b.TimeStart<{}".format(currenthour+1)
        dbcurcorrto.execute(select)
        result = dbcurcorrto.fetchall()
        print(select)
        for row in result:

            startTime=str(row[3])+":"+str(row[4])
            endTime=str(QTime.currentTime().toString("hh:mm"))
            tc.getTime(startTime, endTime)
            timeH,timeM=tc.getTime(startTime, endTime)
            timeH=int(timeH)
            if timeH>=1:
                print(row[0] + "  " + row[1] + "  " + row[2] + "   " + row[3] + "   " + row[4] + "   " + row[5] + "   " +row[6])
                insert = "insert into canclebooking values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(date, row[0], row[1], row[2], row[3], row[4], row[5], row[6], ExTime, Exrs)
                dbcurcorrto.execute(insert)
                dbconnectrto.commit()
                print(row)
                delete = "DELETE FROM logup WHERE CarNo='{}'".format(row[2])
                dbcurcorrto.execute(delete)
                dbconnectrto.commit()
                CarNo = row[2]
                DeteteBooking = "delete from booking where CarNo='{}' ".format(CarNo)
                #Detetelogup = "delete from logup where CarNo='{}'".format(CarNo)
                #Deteteparkcar = "delete  from parkcar where CarNo='{}'".format(CarNo)
                DeleteSloat_1 = "delete  from sloat_info.sloat_1 where CarNo='{}'".format(CarNo)
                DeleteSloat_2 = "delete  from sloat_info.sloat_2 where CarNo='{}'".format(CarNo)
                DeleteSloat_3 = "delete  from sloat_info.sloat_3 where CarNo='{}'".format(CarNo)
                DeleteSloat_4 = "delete  from sloat_info.sloat_4 where CarNo='{}'".format(CarNo)
                DeleteSloat_5 = "delete  from sloat_info.sloat_5 where CarNo='{}'".format(CarNo)
                DeleteSloat_6 = "delete  from sloat_info.sloat_6 where CarNo='{}'".format(CarNo)
                DeleteSloat_7 = "delete  from sloat_info.sloat_7 where CarNo='{}'".format(CarNo)
                DeleteSloat_8 = "delete  from sloat_info.sloat_8 where CarNo='{}'".format(CarNo)
                dbcurcorrto.execute(DeteteBooking)
                print("DeleteBooking")
                dbconnectrto.commit()
                #dbcurcorrto.execute(Detetelogup)
                print("Deletelogup")
                #dbcurcorrto.commit()
                #dbcurcorrto.execute(Deteteparkcar)
                print("Deleteparkcar")
                #dbcurcorrto.commit()
                dbcurcorrto.execute(DeleteSloat_1)
                print("Deletesloat_1")
                dbconnectrto.commit()
                dbcurcorrto.execute(DeleteSloat_2)
                print("Deletesloat_2")
                dbconnectrto.commit()
                dbcurcorrto.execute(DeleteSloat_3)
                print("Deletesloat_3")
                dbconnectrto.commit()
                dbcurcorrto.execute(DeleteSloat_4)
                print("Deletesloat_4")
                dbconnectrto.commit()
                dbcurcorrto.execute(DeleteSloat_5)
                print("Deletesloat_5")
                dbconnectrto.commit()
                dbcurcorrto.execute(DeleteSloat_6)
                print("Deletesloat_6")
                dbconnectrto.commit()
                dbcurcorrto.execute(DeleteSloat_7)
                print("Deletesloat_7")
                dbconnectrto.commit()
                dbcurcorrto.execute(DeleteSloat_8)
                print("Deletesloat_8")
                dbconnectrto.commit()

        dbcurcorrto.close()
        dbconnectrto.close()

    def CheckCancleBook(self,user,Pass1):
        dbconnectRT = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        dbcurcorRT = dbconnectRT.cursor()
        select = "SELECT * from canclebooking where UserName='{}' and  PassWord='{}'".format(user,Pass1)
        print(select)
        dbcurcorRT.execute(select)

        for row in dbcurcorRT:
            print("count")
        return dbcurcorRT.rowcount
        dbconnectRT.commit()
        dbcurcorRT.close()
        dbconnectRT.close()

    def InsertCashBack(self,UserName,CarNo,EndTime,CurrentTime,RemainingTime,CashbakRs):
        dbconnect = mysql.connector.connect(host="localhost", user="root", password="", port="3306",
                                            database="sampledb")
        dbcurcor = dbconnect.cursor()
        Insert = "insert into cashback values('{0}','{1}','{2}','{3}','{4}','{5}');".format(UserName,CarNo,EndTime,CurrentTime,RemainingTime,CashbakRs)
        # print("'{0}','{1}','{2}','{3}'".format(var,var1,var2,var3))
        print(Insert)
        dbcurcor.execute(Insert)
        print("hii")
        dbconnect.commit()
        dbcurcor.close()
        dbconnect.close()

    def CheckBooking(self,old):
        if old==0:
            dbconnect1a = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb")
        if old==1:
            dbconnect1a = mysql.connector.connect(host="localhost", user="root", password="", port="3306",database="sampledb1")
        dbcurcor1a = dbconnect1a.cursor()
        Select = "select * from booking"

        print(Select)
        dbcurcor1a.execute(Select)

        for row in dbcurcor1a:
            print("cnt")
        a=dbcurcor1a.rowcount

        Select = "select * from canclebooking"
        print(Select)
        dbcurcor1a.execute(Select)

        for row in dbcurcor1a:
            print("cnt")
        b= dbcurcor1a.rowcount

        Select = "select * from exitcar"
        print(Select)
        dbcurcor1a.execute(Select)



        for row in dbcurcor1a:
            print("cnt")
        d= dbcurcor1a.rowcount

        Select = "select * from parkcar"
        print(Select)
        dbcurcor1a.execute(Select)

        for row in dbcurcor1a:
            print("cnt")
        e= dbcurcor1a.rowcount

        Select = "select * from rto_payment"
        print(Select)
        dbcurcor1a.execute(Select)

        for row in dbcurcor1a:
            print("cnt")
        f = dbcurcor1a.rowcount
        return (a,b,d,e,f)

