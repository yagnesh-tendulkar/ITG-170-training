try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    try:
        result = a / b
        print("Result =", result)

    except ZeroDivisionError:
        print("Inner Try: Cannot divide by zero")

except ValueError:
    print("Outer Try: Invalid input")