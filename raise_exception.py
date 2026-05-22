def withdraw(balance, amount):

    if amount > balance:
        raise Exception("Insufficient balance")

    return balance - amount


try:
    balance = 5000
    amount = int(input("Enter withdrawal amount: "))

    remaining = withdraw(balance, amount)

    print("Transaction successful")
    print("Remaining balance:", remaining)

except ValueError:
    print("Please enter a valid number")

except Exception as e:
    print(e) 