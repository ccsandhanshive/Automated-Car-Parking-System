
'''def getTime(startTime, endTime):

    hour = 24
    minute = 60

    stime = startTime.split(':')
    etime = endTime.split(':')

    shrs = int(stime[0])
    smin = int(stime[1])

    ehrs = int(etime[0])
    emin = int(etime[1])

    rhrs = 0
    rmin = 0
    try:
        if shrs>hour or ehrs>hour:
            raise
    except:
        print("time value is wrong")
    if shrs <= hour and ehrs <= hour:
        if emin < minute and smin < minute :
            if shrs < ehrs:
                rhrs = ehrs - shrs
            elif ehrs==shrs:
                rhrs=0
            else:
                if shrs == hour:
                    rhrs = ehrs
                    print(rhrs)
                else:
                    rhrs = (hour - shrs) + ehrs
                    print(rhrs)
            if emin < smin:
                rmin = emin - smin

            if (emin+smin)>minute:
                rhrs+=1
                rmin = rmin-minute

            else:
                rmin=emin+smin
                if shrs==hour:
                    shrs=0
                    rmin=minute-smin
                if abs(ehrs-shrs)==1:
                    rhrs=0
                    rmin = minute - smin
                if ehrs==shrs:
                    rmin=emin-smin

    if rhrs<10: rh = "0"+str(rhrs)
    else: rh=str(rhrs)
    if rmin <10:rm = "0"+str(rmin)
    else: rm=str(rmin)

    return (rh, rm)

hrs, mins = getTime("01:30","02:30")
print("HRS : {}, MIN : {}".format(hrs,mins))



"""import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", password="", database="sampledb")
cur = db.cursor()
cur.execute("SELECT * FROM BOOK")
for val in cur :
    hr, minu = getTime(val[2],val[3])
    print("{} \t |{}| \t |{}| \t |{}| Total Time = {}:{}".format(val[0],val[1],val[2],val[3],hr,minu))

cur.close()
db.close()"""
'''
from PyQt5.QtCore import *
import booking_db as db
#db.BookDB().InsertCancleBooking(14-10-2018,17,"----","----")
a=db.BookDB().CheckCarExit("mh123456")
print(a)
#db.BookDB().DeleteAllRecords("lllll")
print(QDate.currentDate().toString("dd-MM-yyyy"))
print(QTime.currentTime().hour())

'''a,b,c,d,e,f=db.BookDB().CheckBooking()
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)'''
#print(QDate.currentDate().toString("dd-MM-yyyy"))
#print(QDate.currentDate().toString("dd-MM-yyyy"))
#print(QTime.currentTime().minute())
#print(QTime.currentTime().toString("hh:mm"))