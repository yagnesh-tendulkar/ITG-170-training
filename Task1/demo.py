n=5
val=15
for i in range(n,0,-1):
    for j in range(i):
        print(val,end=" ")
        val-=1
    print()