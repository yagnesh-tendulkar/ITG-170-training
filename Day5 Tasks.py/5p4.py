try:
    a = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Finally block always executes")