num= int(input("Enter a number: "))
big=0
while num>0:
    rem= num%10
    if big<rem:
        big=rem
    num=num//10
print(big)