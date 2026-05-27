arr = list(map(int, input("Enter elements: ").split()))

print("Even numbers:")
for i in arr:
    if i % 2 == 0:
        print(i, end=" ")

print("\nOdd numbers:")
for i in arr:
    if i % 2 != 0:
        print(i, end=" ")