num= int(input('Enter a number: '))
digit = int(input('Enter a digit: '))
count=0

while num >0:
    rem = num %10
    if rem == digit:
        count+=1
    num = num //10
print(count)
