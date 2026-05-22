try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integer numbers.")

finally:
    print("Program execution completed.")