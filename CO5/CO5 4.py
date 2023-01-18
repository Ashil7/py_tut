import csv
csvf=open('studentdetails.csv','r')
csvr=csv.reader(csvf)
print(csvr)