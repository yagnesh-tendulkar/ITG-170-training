num= int(input('Enter a number: '))

def reverseNumber(num):
    rev=''
    while num>0:
        rem = num%10
        rev+=str(rem)
        num = num//10
    return rev
print(reverseNumber(num))