#Create a Bank account with members account number, name, type of account and balance. 
# Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class BankAccount:
    def __init__(self,AccNo,AccName,AccType,AccBalance=0):
        self.number=AccNo
        self.Name=AccName
        self.Atype=AccType
        self.Balance=AccBalance
    def withdraw(self,Amount):
        if( Amount>=self.Balance ):
            print("Low balance")
        else:
            self.Balance= self.Balance-Amount    
    def deposit(self,Amount):
        self.Balance= self.Balance+Amount    
    def display(self):
        print("Account Number: ",self.number)
        print("Account Name: ",self.Name)
        print("Account type: ",self.Atype)
        print("Account Balance: ",self.Balance)

accno=int(input("Enter your acc No:"))
name=input("Enter your Name:")
obj =BankAccount(accno, name, "Savings")
print("\n1.Account info\n2.Deposit\n3.Withdraw\n4.Exit")
while(1):
    
    opt=int(input("Select your option:"))
    if opt == 1:
        obj.display()
    elif opt == 2:
        dep=int(input("Enter the value to deposite: "))
        obj.deposit(dep)
        print("Account Balance: ",obj.Balance)
    elif opt == 3:
        wid=int(input("Enter the value to withdraw: "))
        obj.withdraw(wid)
        print("Account Balance: ",obj.Balance)
    elif opt == 4:
        print("Exit")
        break
    else:
        print("Invalid Option")
