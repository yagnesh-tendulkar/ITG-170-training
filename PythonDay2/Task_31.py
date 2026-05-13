arr = []
r = int(input("Enter the range :"))
for i in  range(1,r+1):
    n = int(input("Enter the element :"))
    arr.append(n)
largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i<smallest:
        smallest = i
print("The largest element is",largest)
print("The smallest element is",smallest)