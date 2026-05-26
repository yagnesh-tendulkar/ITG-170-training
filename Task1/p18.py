num=int(input("Enter the number : "))
temp=num
last=num%10
while temp>10:
    temp=temp//10
first=temp
print(last+first)