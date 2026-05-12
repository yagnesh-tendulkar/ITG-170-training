n = 5

for i in range(1, n + 1):

    # Left spaces
    for j in range(n - i):
        print(" ", end="")

    # Stars
    for k in range(i):
        print("* ", end="")

    print()