n = int(input("Enter the n value: "))
arr = []
for i in range(n):
    val = int(input("Enter the val: "))
    arr.append(val)
max_digit=0
for i in range(n):
    if arr[i]>max_digit:
        max_digit=arr[i]
print(max_digit)
small_digit=arr[0]
for i in range(n):
    if arr[i]<small_digit:
        small_digit=arr[i]
print(small_digit)
