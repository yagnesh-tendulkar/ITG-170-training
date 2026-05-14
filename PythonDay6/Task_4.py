def num(n):
    for i in range(1,n+1):
        yield i
for i in num(5):
    print(i)
