a= input("Please Enter First String : ")
b =input("Please Enter Second String : ")

c=a[0]
a=a.replace(a[0],b[0])
b=b.replace(b[0],c)

print(a," ",b)
