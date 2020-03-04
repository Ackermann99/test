# -*- coding: utf-8 -*-
import csv
f=open("CSVex.csv",'a',newline="")
wr=csv.writer(f)
wr.writerow(['Name','Age'])
ch=0
while(ch!= -1):
    name=input("Enter name : ")
    age=input("Enter age : ")
    wr.writerow([name,age])
    ch=int(input("Enter -1 to exit "))
f.close()

