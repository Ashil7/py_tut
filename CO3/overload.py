class moverload:
    def display(self,a=None,b="Done"):
        print(a,b)
obj=moverload()
obj.display()
obj.display(10)
obj.display(10,20)
    