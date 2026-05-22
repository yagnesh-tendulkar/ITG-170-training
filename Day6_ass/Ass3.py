#Write a program to handle exceptions with Nested Try.
try:
    accno=int(input("Enter accno:"))
    try:
        password=input("Enter password:")
        if password != "admin123":
            raise ValueError("Incorrect password")

        print("Balance is 10000")

    except ValueError as e:
        print(e)

except ValueError:
    print("Invalid account number")