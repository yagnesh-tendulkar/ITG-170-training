import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

end= int(input('Enter the end of limit: '))
for i in range(1,end+1):
    if isPrime(i):
        print(i)

