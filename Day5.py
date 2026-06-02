# Program 1 : Exceptions Using Try-Except Block
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

# Program 2 : Exceptions with Multiple Except Blocks
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    my_list = [10, 20, 30]

    print("Result =", result)
    print("Element =", my_list[5])

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

except IndexError:
    print("Error: List index out of range")

except Exception as e:
    print("Some other error occurred:", e)

# Program 3 : Handle Exceptions with Nested Try
try:
    print("Outer try block")

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2

        print("Result =", result)

    except ZeroDivisionError:
        print("Inner Exception: Cannot divide by zero")

except ValueError:
    print("Outer Exception: Invalid input")

# Program 4 : Finally Block
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Finally block executed")
