try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("This block always executes")