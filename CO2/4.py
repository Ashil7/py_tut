from math import sqrt
n=int(input("Enter the limit :"))

a=[ i for i in range(1000,n)
    if sqrt(i)==int(sqrt(i)) and i%2==0]
print(a)    
