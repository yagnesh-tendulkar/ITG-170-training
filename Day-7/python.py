n = 3

# upper part
for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for d in range(i, 0, -1):
        print(d, end="")

    for a in range(2, i + 1):
        print(a, end="")

    print()

# lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    for d in range(i, 0, -1):
        print(d, end="")

    for a in range(2, i + 1):
        print(a, end="")

    print()