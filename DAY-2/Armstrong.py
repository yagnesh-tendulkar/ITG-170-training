for i in range(1, 1001):
    n = i
    s = 0

    while n > 0:
        d = n % 10
        s = s + d ** 3
        n = n // 10

    if s == i:
        print(i)
