import calculator


print("Calculator")
print("a.Add")
print("b.sub")
print("c.Mul")
print("d.Div")
c=input("Please enter your choice (a/b/c/d):")

a=int(input("Enter NO 1 :"))
b=int(input("Enter NO 2 :"))

if c=='a':
    print(a,"+",b,"=",calculator.add(a,b))
elif c=='b':
    print(a,"-",b,"=",calculator.sub(a,b))
elif c=='c':
    print(a,"*",b,"=",calculator.mul(a,b))
elif c=='d':
    print(a,"/",b,"=",calculator.div(a,b))
    
else:
    print("Not valid")