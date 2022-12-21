n=int(input("LIMIT :"))

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
    
for i in reversed(range(0,n)):
    for j in reversed(range(0,i)):
        print("*",end=" ")
    print("\n")
        