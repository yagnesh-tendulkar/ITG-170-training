#.Program to sort the elements of an array in descending order.
arr=[1,2,3,5,4,9,6,8,7]
n=len(arr)
temp=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Descending order:")
for i in arr:
    print(i)
