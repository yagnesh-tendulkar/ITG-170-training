print("--------writing code to print the prime number from m to n-----------")

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

M=int(input("Enter the Number from M "))
N=int(input("Enter the Number upto N "))
for i in range(M,N):
    if prime(i):
        print(i)