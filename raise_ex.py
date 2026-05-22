try:
    balance=50000
    amount=int(input("enter amount"))
    if amount>balance:
        raise Exception("insufficient balance")
    elif amount<=0:
        raise Exception("enter valid amount")
    else:
        balance=balance-amount
        print("transaction successful")
        print(f"remaining balance is {balance}")
except ValueError:
    print("enter valid value")
