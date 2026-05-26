n=int(input("Enter the n value :"))
for i in range(1,n+1):
    for sp in range(n-i):
        print(" ",end=" ")
    for st in range(i,0,-1):
        print(st,end=" ")
    for st2 in range(2,i+1):
        print(st2,end=" ")
    print()