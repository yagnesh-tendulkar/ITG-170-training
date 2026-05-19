try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print(a/b)
except ZeroDivisionError as e:
    print(e)
finally:
    print("You can run again")