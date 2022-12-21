from Graphics.Rectangle import*
from Graphics.Circle import*
from Graphics.dGraphics.Cuboid import*
from Graphics.dGraphics.Sphere import*

l=int(input("Enter Length :"))
b=int(input("Enter Breadth :"))
print("Area of Rectangle :",rArea(l,b))
print("Perimeter of Rectangle :",rPeri(l,b))

r=int(input("Enter Radius :"))

print("Area of Circle",cArea(r))
print("Perimeter of Circle",cPeri(r))

l=int(input("Enter Length :"))
w=int(input("Enter Width :"))
h=int(input("Enter Height :"))

print("Area of Cuboid :",CuArea(l,w,h))
print("Perimeter of Cuboid:",CuPeri(l,w,h))

r=int(input("Enter Radius :"))
 
print("Area of Sphere :",sArea(r))
print("Perimeter of Sphere :",sPeri(r))





