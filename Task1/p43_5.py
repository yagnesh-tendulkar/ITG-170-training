n=int(input("Enter the n value : "))
for i in range(1,n+1):
    val=n
    for j in range(i):
        print(val,end=" ")
        val-=1
    print()