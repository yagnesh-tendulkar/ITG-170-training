n = 3

# upper
for i in range(1, n + 1):

    print(" " * (n - i), end="")

    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

# lower
for i in range(n - 1, 0, -1):

    print(" " * (n - i), end="")

    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")