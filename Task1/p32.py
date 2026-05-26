n = int(input("Enter the n value: "))
arr = []
for i in range(n):
    val = int(input("Enter the val: "))
    arr.append(val)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Order : ",arr)


