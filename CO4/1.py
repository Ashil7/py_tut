class rectangle:
    def __init__(self , length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
    def area(self):
        return self.length*self.breadth
    def compare(self,obj2):
        try:
            if obj1.area()==obj2.area():
                print("Both Equal")
            elif obj1.area()>obj2.area():
                print("Rectangle 1 is Bigger")
            else:
                print("Rectangle 2 is Bigger")
        except:
            print("Raised")
    
        
l1=int(input("L1:"))
b1=int(input("B1:"))
l2=int(input("L2:"))
b2=int(input("B2:"))
obj1=rectangle(l1,b1)
obj2=rectangle(l2,b2)
print("Area 1:",obj1.area())
print("ARea 2 :",obj2.area())
print("Perimeter 1:",obj1.perimeter())
print("Perimeter 2:",obj2.perimeter())
obj1.compare(obj2)