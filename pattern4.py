number=int(input("enter number : "))
for i in range(number):
    for j in range(i+1):
        print(number-j,end='')
    print()    