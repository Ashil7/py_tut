l=int(input("Enter length:"))
b=int(input("Enter Breadth:"))
h=int(input("Enter height:"))
r=lambda x,y: x*y
s=lambda x: x*x
t=lambda x,y: 0.5*x*y
print("Area of rectangle",r(l,b))
print("Area of square",s(l))
print("Area of triangle",t(b,h))

        