#Program to print the elements of an array in reverse order without sorting.
arr = [10, 20, 30, 40, 50]

print("Array elements in reverse order:")

for i in range(len(arr) - 1, -1, -1):
    print(arr[i])