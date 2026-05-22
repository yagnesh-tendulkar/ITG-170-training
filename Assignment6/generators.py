def gen(n):
    i=1
    while i <= n:
        yield i
        i += 1
n = gen(10)
for i in n:
    print(i)