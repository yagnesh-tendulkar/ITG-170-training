n = int(input("Enter how many perfect numbers to print: "))

count = 0
num = 1

while count < n:
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num, end=" ")
        count += 1

    num += 1