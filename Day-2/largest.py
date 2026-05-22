arr = [12, 45, 7, 89, 23, 5]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest number is:", largest)
print("Smallest number is:", smallest)
