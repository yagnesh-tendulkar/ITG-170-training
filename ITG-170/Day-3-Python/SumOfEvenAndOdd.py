num= int(input('Enter the number: '))
evenSum=0
oddSum=0
while num>0:
    rem=num%10
    if rem%2==0:
        evenSum=evenSum+rem
    else:
        oddSum=oddSum+rem
    num= num//10
print('Even Sum: ',evenSum)
print('Odd Sum: ',oddSum)