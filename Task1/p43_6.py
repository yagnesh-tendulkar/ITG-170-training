n=int(input("Enter the n value : "))
val=1
for i in range(1,n+1):
    for i in range(i):
        print(val,end=" ")
        val+=1
    print()