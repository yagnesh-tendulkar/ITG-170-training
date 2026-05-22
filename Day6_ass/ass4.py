#Write a program to execute a statement using Finally Block.
try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    result = n1 / n2

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter valid numeric value")

finally:
    print("Program execution completed")