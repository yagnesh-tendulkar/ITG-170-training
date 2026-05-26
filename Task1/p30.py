n = int(input("Enter the n value: "))

arr = []

for i in range(n):
    val = int(input("Enter the val: "))
    arr.append(val)

arr2 = []

i = n - 1

while i >= 0:
    arr2.append(arr[i])
    i = i - 1

print(arr2)


for i in range(n):
    for j in range(i + 1, n):

        if arr2[i] > arr2[j]:
            temp = arr2[i]
            arr2[i] = arr2[j]
            arr2[j] = temp
print(arr2)