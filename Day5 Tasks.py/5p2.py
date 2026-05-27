try:
    a = int(input("Enter number: "))
    b = 10 / a
    print(b)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter only numbers")