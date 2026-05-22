class Insufficientbalance(Exception):
    pass

balance=1000
withdrawl=int(input("enter amount:"))
if withdrawl>balance:
    raise Exception('insufficient balance')
else:
    print("withdrawl successful")