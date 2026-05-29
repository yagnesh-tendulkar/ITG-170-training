# #abstractclass scenario:Payment system
# Create an abstract class called Payment.

# It should contain:

# an abstract method called pay()

# Create child classes:

# CreditCard
# UPI
# Cash

# Each class should implement the pay() method differently.
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class Creditcard(Payment):
    def pay(self,amount):
        print(f"Paying {amount} using Credit Card")
class UPI(Payment):
    def pay(self,amount):
        print(f"{amount} paid using UPI")
class Cash(Payment):
    def pay(self,amount):
        print(f"{amount} paid in cash")
cashier=Cash()
cashier.pay(2000)
card=Creditcard()
card.pay(5000)
upi=UPI()
upi.pay(1000)
