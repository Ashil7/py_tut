import csv
p=[('lata',22,45),('Anil',21,56),('John',20,60)]
csvfile=open("new.csv",'w',newline='')
obj=csv.writer(csvfile)
obj.writerows(p)
csvfile.close()

    