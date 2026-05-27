t = tuple(map(int,input("Enter numbers:").split()))
repeated = set()
for i in t:
    if t.count(i) > 1:
        repeated.add(i)
print(repeated)