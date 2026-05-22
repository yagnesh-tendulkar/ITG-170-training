# Create generator for squares till N
def gen(n):
    i=1
    while i <= n:
        val = i * i
        i += 1
        yield val
n = gen(10)
for i in n:
    print(i)