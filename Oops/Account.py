class Account:
    def __init__(self,ac_holder,balance):
        self.ac_holder=ac_holder
        self.balance=balance
    def deposit(self,amount):
        if amount<=self.balance:
            print("Enter the sufficient ammount : ")
        else:
            self.balance+=amount
            print("Total balance : ",self.balance)
    def withdraw(self , amount):
        if amount>=self.balance:
            print("Enter the correct ammount : ")
        else:
            self.balance-=amount
            print("Balance Amount : ",self.balance)
class Saving(Account):
    def __init__(self, ac_holder="Ram", balance=0):
        super().__init__(ac_holder, balance)
       # self.intrest=intrest
    def intrest(self,intrest_rate):
        intrest_amount=(self.balance*intrest_rate)/100
        self.balance=self.balance+intrest_amount
        print("Updated balance : ",self.balance)
s=Saving()
s.deposit(200)
s.withdraw(13)
s.intrest(5)



        