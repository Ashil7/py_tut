a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))

if a>b:
    if a>c:
        print("A biggest")
    else:
        print("C biggest")
elif b>c:
    print("B biggest")
else:
    print("C biggest")