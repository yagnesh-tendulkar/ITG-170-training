try:
    try:
        a=int(input("enter the value of a:"))
        print(a/0)
    except ZeroDivisionError:
        print("cant divide by zero")
except ValueError:
    print("invalid input")