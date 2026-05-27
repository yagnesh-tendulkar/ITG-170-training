arr = list(map(int, input("Enter elements: ").split()))

visited = []

for i in arr:
    if i not in visited:
        print(i, "->", arr.count(i))
        visited.append(i)