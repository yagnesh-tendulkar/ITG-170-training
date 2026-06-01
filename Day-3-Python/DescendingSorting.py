arr=[2,5,6,3,0,9,4,8,1]

for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
print(arr)