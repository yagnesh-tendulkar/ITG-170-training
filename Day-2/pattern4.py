rows = 5

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))
