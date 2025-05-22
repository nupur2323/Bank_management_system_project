class ATM:
    def __init__(self,name,account_no,balance):
        self.name=name
        self.account_no=account_no
        self.balance=balance
    
    def withdraw(self,amount):
        if amount<self.balance:      
            self.balance-=amount
            print("Amount withdraw sucessfully !!")
            print(f"Account Balance : {self.balance}")
        else:
            print("Insufficient balance in the account !! Try again!!")
    def deposite(self,amount):
        self.balance+=amount
        print("Amount deposited succesfully!!")
        print(f"Account Balance: {self.balance}")
    def check_balance(self):
        print(f"Account Balance: {self.balance}")

obj1=ATM("Nupur",1234,50000)
while True:
    print("""
          1)Check balance
          2)Withdraw amount
          3)Deposite amount
          4)exit
          """)
    ch=int(input("enter the choice:  "))
    if ch==1:
        obj1.check_balance()
    elif ch==2:
        am=eval(input("enter the amount to be withdraw: "))
        obj1.withdraw(am)
    elif ch==3:
        am=eval(input("enter the amount to be deposite: "))
        obj1.deposite(am)
    elif ch==4:
        break
    else:
        print("Invalid Choice !!")