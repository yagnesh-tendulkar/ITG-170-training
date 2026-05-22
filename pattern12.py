row=int(input("enter number of rows ."))
ch=65
for i in range(row):
    for j in range(i+1):
        print(chr(ch+j),end=" ")
    print()      