

#def addTime(start,end):
#def subTime(start,end):
#def getAvailability(timefrom, timeto):
def getTime(startTime, endTime):		#for time calculation


    stime = startTime.split(':')			##split time by :
    etime = endTime.split(':')

    shrs = int(stime[0])
    smin = int(stime[1])

    ehrs = int(etime[0])
    emin = int(etime[1])

    rhrs=0
    rmin=0


    if smin > emin:			#if starting min is greter than ending minite
        ehrs = ehrs - 1		# 		then ending hrs -1
        emin = emin + 60	#			 ending min+60
    mins = emin - smin		#minite = ending min - starting minite
    hrs = ehrs - shrs		#houres= ending houres - sharting houres

    rh=str(hrs)
    rm=str(mins)

    return (rh, rm)			#Return remaining hours and minites



#hrs, mins = getTime("05:00","07:00")
#print("HRS : {}, MIN : {}".format(hrs,mins))



"""import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", password="", database="sampledb")
cur = db.cursor()
cur.execute("SELECT * FROM BOOK")
for val in cur :
    hr, minu = getTime(val[2],val[3])
    print("{} \t |{}| \t |{}| \t |{}| Total Time = {}:{}".format(val[0],val[1],val[2],val[3],hr,minu))

cur.close()
db.close()"""
