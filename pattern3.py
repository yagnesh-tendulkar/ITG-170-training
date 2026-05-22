number=int(input("enter number of rows"))
val=1;
for i in range(number):
    for j in range(i+1):
        print(val,end=' ')
        val=val+1;
    print()  