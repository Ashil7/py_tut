n=(int(input("LIMIT :")))
a=[]
for i in range(0,n):
    b=(int(input("Enter Data :")))
    a.append(b)
print(a)
sum=0
for j in a:
    sum=sum+j
print("SUM :",sum)