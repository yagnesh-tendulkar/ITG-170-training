#Find big digit in a number.
num=int(input("ENter a value:"))
largest=0
smallest=9
while (num):
    digit=num%10
    largest=max(digit,largest)
    num=num/10
print("largest digit is :",largest)