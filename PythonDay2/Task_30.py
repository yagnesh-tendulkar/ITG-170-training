arr = []
r = int(input("enter range of array: "))
for i in range(1,r+1):
    n = int(input("enter number: "))
    arr.append(n)
arr1=[]
print("Array in reverse order: ")
for i in range(r-1,-1,-1):
    arr1.append(arr[i])
print(arr1)