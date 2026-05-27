arr = list(map(int, input("Enter elements: ").split()))

print("Reversed array:")
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")