m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

for num in range(m, n + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")