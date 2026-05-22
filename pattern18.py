n = 4

# upper part
for i in range(1, n + 1):

    for space in range(i - 1):
        print(" ", end="")

    for j in range(i, n + 1):
        print(j, end=" ")

    print()

# lower part
for i in range(n - 1, 0, -1):

    for space in range(i - 1):
        print(" ", end="")

    for j in range(i, n + 1):
        print(j, end=" ")

    print()