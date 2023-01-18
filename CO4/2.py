class BankAccount:
    def __init__(self,acno,name,atype,balance):
        self.acno=acno
        self.name=name
        self.atype=atype
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
x=BankAccount(12344,"Ash","reg",1500)
print("Details")
print()