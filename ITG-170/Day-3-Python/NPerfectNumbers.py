n= int(input('Enter how many perfect number you want: '))
count=0
def isPerfectNumber(num):
    total=0
    for i in range(1, num):
        if num % i == 0:
            divisor = i
            total += divisor

    if total == num:
        return True
    else:
        return False
num=1
while count<n:
    if isPerfectNumber(num):
        print(num)
        num+=1
        count+=1
    else:
        num+=1