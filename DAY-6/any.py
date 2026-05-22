numbers = [5, 10, -3, 8]

if any(num < 0 for num in numbers):
    print("List contains a negative number")
else:
    print("No negative numbers found")