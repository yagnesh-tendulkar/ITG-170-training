#Write a program to handle exceptions with Throws Keyword.
def divide(a, b):

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


try:
    result = divide(10, 6)

    print("Result:", result)

except ZeroDivisionError as e:
    print(e)