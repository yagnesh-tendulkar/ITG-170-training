try:
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    print(a/b)
except ZeroDivisionError:
    print("division by zero not possible")
except ValueError as e:
    print(e)
