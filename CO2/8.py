n=int(input("LIMIT :"))
a=[]
for i in range(n):
    b=input("Enter data:")
    a.append(b)
print(a)
m=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>m):
        m=len(i)
        temp=i
print("length of longest word is ",m, "and word is",i)