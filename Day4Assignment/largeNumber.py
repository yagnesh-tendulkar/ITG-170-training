def LargestNumber(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return f"both are same number{a}"
    
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(LargestNumber(a,b))

