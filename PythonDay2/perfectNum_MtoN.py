print("========:Perfect number logic from m to n:========")

def perfect_number(n):
    if n<=0:
        return False
    
    count=0
    for i in range(1,n):
        if n%i==0:
            count+=i

    if count==n:
        print(f"It's a perfect number {n}")
    else:
        print("not a perfect number")


N=int(input("Enter N : "))
M=int(input("Enter M"))
for i in range(M,N+1):
    if perfect_number(i):
        print(i)
