try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")