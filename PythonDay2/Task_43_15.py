n = 7

for i in range(1, n + 1):


    for j in range(1, i):
        print("*", end="")

    print(i, end="")

    for j in range(1, i):
        print("*", end="")

    print()