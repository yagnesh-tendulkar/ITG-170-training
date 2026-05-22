n = int(input())

def sq_sum(x):
    s = 0
    while x > 0:
        d = x % 10
        s += d * d
        x //= 10
    return s

seen = []

while n != 1 and n not in seen:
    seen.append(n)
    n = sq_sum(n)

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
