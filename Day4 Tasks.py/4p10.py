s = set(map(int, input("Enter elements: ").split()))
item = int(input("Enter item to remove: "))
if item in s:
    s.remove(item)
    print("Updated set:", s)
else:
    print("Item not present")