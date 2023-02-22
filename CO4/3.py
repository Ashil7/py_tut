class rectangle:
    def __init__(self,len,bre):
        self.__len=len
        self.__bre=bre
    def area(self):
        return (self.__len*self.__bre)
    def __lt__(self, other):
        if r1.area()>other.area():
            print("r1")
        else:
            print("r2")
l=int(input("length:"))
b=int(input("breadth:"))
r1=rectangle(l,b)
print("area",r1.area())

l=int(input("length:"))
b=int(input("breadth:"))
r2=rectangle(l,b)
print("area",r2.area())

r1<r2