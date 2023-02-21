#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.


import csv

student =[{'No':1,'name':'Ashil','role':'student'}]
csv_f =open('Name.csv','w')
field_name= list(student[0].keys())

csv_w  =csv.DictWriter(csv_f,fieldnames=field_name)
csv_w.writeheader()+
csv_w.writerows(student)
csv_f.close()
