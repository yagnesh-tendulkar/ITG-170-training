n=int(input("Enter the n value"))
for i in range(1,n+1):
    for sp in range(n-i):
        print(" ",end=" ")
    for st in range(2*i-1):
        print("*",end=" ")
    print()