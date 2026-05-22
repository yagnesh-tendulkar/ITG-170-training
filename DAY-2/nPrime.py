n = int(input())
c = 0
num = 2
while c < n:
    f = 0
    for i in range(2, num):
        if num % i == 0:
            f = 1
            break
    if f == 0:
        print(num)
        c += 1
    num += 1
