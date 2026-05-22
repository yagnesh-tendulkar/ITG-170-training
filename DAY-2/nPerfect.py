n = int(input())
c = 0
num = 1
while c < n:
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    if s == num:
        print(num)
        c += 1
    num += 1
