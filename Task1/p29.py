n=int(input("Enter the n value : "))
arr=[]
for i in range(n):
    val=int(input("Enter the val : "))
    arr.append(val)
for i in range(n):
    count=0
    for j in range(n):
        if arr[i]==arr[j]:
            count+=1
    if count>1 and i==arr.index(arr[i]):
        print("Duplicate :",arr[i])
