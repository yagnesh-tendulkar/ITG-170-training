def isEven(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

print(isEven(int(input('Enter a number: '))))