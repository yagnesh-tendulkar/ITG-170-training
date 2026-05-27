try:
    a = int(input("Enter number: "))
    try:
        b = 10 / a
        print(b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
    print("Invalid input")