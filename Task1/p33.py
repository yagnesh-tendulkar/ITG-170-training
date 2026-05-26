n = int(input("Enter the n value: "))
arr = []
for i in range(n):
    val = int(input("Enter the val: "))
    arr.append(val)
sum=0
for i in range(n):
    sum=sum+arr[i]
print(sum)