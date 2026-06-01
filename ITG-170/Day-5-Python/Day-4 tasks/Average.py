def avg(num1,num2,num3):
    return (num1+num2+num3)/3

try:
    print(avg(int(input('Enter a number: ')),int(input('Enter another number: ')),int(input('Enter another number: '))))
except Exception as e:
    print(e)