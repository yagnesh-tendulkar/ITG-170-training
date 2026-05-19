try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    try:
        c=a/b
        print(c)
    except ZeroDivisionError as e:
        print(e)
except ValueError as e:
    print(e)