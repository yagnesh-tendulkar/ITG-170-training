n = int(input("Enter the n value: "))
arr = []
for i in range(n):
    val = int(input("Enter the val: "))
    arr.append(val)
print("Even number : ")
for i in range(n):
    if arr[i]%2==0:
        print(arr[i],end=" ")
print("\nOdd number : ")
for i in range(n):
    if arr[i]%2!=0:
        print(arr[i],end=" ")