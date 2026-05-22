m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))

print("Prime numbers between", m, "and", n, "are:")

for num in range(m, n + 1):

    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
