arr = []
r = int(input("Enter the range of the array: "))
for i in range(1, r+1):
    n = int(input("Enter the elements of the array: "))
    arr.append(n)
for i in arr:
    if i %2!=0:
        print(i,"is odd")
    else:
        print(i,"is even")