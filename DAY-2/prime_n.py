def q22():
    n = int(input("How many prime numbers? "))
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()