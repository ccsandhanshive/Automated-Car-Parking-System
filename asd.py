import csv
import pandas as pd

with open('exp4.csv','w') as csvfile:
    spamwriter=csv.writer(csvfile,delimiter=',')

    spamwriter.writerow(['s.no','rno','name','age'])
    spamwriter.writerow(['1','3101','Adarsh','20'])
    spamwriter.writerow(['2','3102','Keshav','20'])
    spamwriter.writerow(['3','3103','Akash','19'])
