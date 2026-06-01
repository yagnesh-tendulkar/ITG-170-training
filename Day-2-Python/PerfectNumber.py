num= int(input("Enter a number: "))
total=divisor=0
for i in range(1,num):
    if num%i==0:
        divisor=i
        total+=divisor

if total==num:
    print("It is a perfect number")
else:
    print("Not a perfect number")