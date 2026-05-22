#Program to print n prime numbers.
num=int(input("Enter a number: "))
count=0
i=2
while count<num:
    prime=True
    for j in range (2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i)
        count+=1
    i+=1