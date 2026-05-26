class payment:
    def payment(self,amount):
        self.amount=amount
class upi(payment):
    def payment(self, amount):
        print(f"Paid the amount of {amount} using upi")
class credit(payment):
    def payment(self, amount):
        print(f"Payment made through credit of {amount}")
class netbanking(payment):
    def payment(self, amount):
        print(f"Payment made through net banking {amount}")
n=netbanking()
n.payment(1000)
c=credit()
c.payment(2000)
