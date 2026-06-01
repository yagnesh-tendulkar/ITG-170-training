def isPrime(n):
    count=0;
    for i in range(1,n):
        if n%i==0:
            count+=1
    if count>2:
        return False
    else:
        return True
number=int(input('Enter a number: '))
if isPrime(number):
    print('Prime')
else:
    print('Not Prime')
