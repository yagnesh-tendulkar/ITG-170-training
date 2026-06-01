def findGreater(num1,num2):
    if num1==num2:
        return 'both are same'
    elif num1>num2:
        return num1
    else:
        return num2


print(findGreater(int(input('Enter a number: ')), int(input('Enter another number: '))))