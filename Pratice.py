n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end = " ")
    for k in range(1,1+i):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end = " ")
    for k in range(1,1+i):
        print(k,end=" ")
    for l in range (i-1,0,-1):
        print(l,end=" ")
    print()