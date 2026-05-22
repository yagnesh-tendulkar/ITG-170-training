try:
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
except ZeroDivisionError:
    print("cant divide with zero")
except ValueError:
    print("enter valid value")
except TypeError:
    print("enter correct type")