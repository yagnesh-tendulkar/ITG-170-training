num=1
rows=5
for i in range(1,6):
    for j in range(4-i,-1,-1):
        print(" ",end="")
    for k in range(i):
        print(k+1,end="")
    for l in range(i-2,-1,-1):
        print(l+1,end="")
    print()
for i in range(rows-1,0,-1):
    for j in range(4-i,-1,-1):
        print(" ",end="")
    for k in range(i):
        print(k+1,end="")
    for l in range(i-2,-1,-1):
        print(l+1,end="")
    print()