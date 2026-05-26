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
    print(f"{arr[i]} accurs in {count} times")