try:
    a=int(input("enter a value:"))
    print(a/0)
except ZeroDivisionError:
    print("zero divison error")