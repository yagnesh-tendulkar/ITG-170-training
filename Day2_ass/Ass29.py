#Program to print the duplicate elements of an array.
arr = [1, 2, 3, 2, 4, 5, 1, 6]

print("Duplicate elements are:")

for i in range(len(arr)):

    for j in range(i + 1, len(arr)):

        if arr[i] == arr[j]:
            print(arr[j])
            break