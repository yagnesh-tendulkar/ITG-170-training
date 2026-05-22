try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except ValueError:
    print("Invalid input! Please enter only numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except NameError:
    print("Variable is not defined.")

except Exception as e:
    print("Some other error occurred:", e)