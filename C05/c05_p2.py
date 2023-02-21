#Python program to copy odd lines of one file to other***

f1=open("f1.txt",'r')
f2=open("f2.txt",'w')
l1 =f1.readlines()


for i in range(0,len(l1)):
    if i%2 ==0:
        f2.write(l1[i])
f2.close()
f3=open("f2.txt",'r')
cont =f3.readlines()
print(cont)
f3.close()
