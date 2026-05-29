#try-except-else
try:
    pin=int(input("ENter your PIN:"))
    if pin!=1234:
        raise ValueError("Enter correct PIN!!")
except ValueError :
    print("Invalid PIN. Please enter a valid PIN.")
else:
    print("LoggedIn successfully!!")
finally:
    print("Thank you for using our service!!")