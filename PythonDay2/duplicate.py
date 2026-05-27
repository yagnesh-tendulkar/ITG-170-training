print("===============duplicate elements of an array=======================")

arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    if arr[i] in arr[i+1:n]:
        print(f"Duplicate value found which is {arr[i]}")
    