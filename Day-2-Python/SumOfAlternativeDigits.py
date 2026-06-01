num= int(input('Enter a number: '))
total=0
while num>0:
    rem= num%10
    total+=rem
    num=num//100
print(total)