#Create a class Publisher (name).
#Derive class Book from Publisher with attributes title and author.
#Derive class Python from Book with attributes price and no_of_pages. 
#Write a program that displays information about a Python book.
#Use base class constructor invocation and method overriding.

class Publisher():

    def __init__(self,t,n):
        self.__title=t
        self.__author=n
    def display(self):
        print("Title =",self.__title)
        print("author =",self.__author)    
class Book(Publisher):
    
    def __init__(self,t,n,p,np):
        super().__init__(self,t,n)
        self.__price=p
        self.__no_of_page=np
        
    def display(self):
        print("price =",self.__price)
        print("no_of_page =",self.__no_of_page)
class Python(Book):
    def __init__(self,t,n,p,np):
        self.__title=t
        self.__author=n
        self.__price=p
        self.__no_of_page=np
    def display(self):
        print("Title =",self.__title)
        print("author =",self.__author)
        print("price =",self.__price)
        print("no_of_page =",self.__no_of_page)   

obj =Python("book1","nam1",1000,100)
obj.display()
        