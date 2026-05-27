print("==================program to print n prime number====================")

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True


N=int(input("Enter the number upto n : "))
for i in range(1,N):
    if prime(i):
        print(i)