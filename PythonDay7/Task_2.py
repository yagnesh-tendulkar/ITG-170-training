try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError as e:
    print("Zero Division Error: ",e)
except ValueError as e:
    print("Invalid Value",e)
