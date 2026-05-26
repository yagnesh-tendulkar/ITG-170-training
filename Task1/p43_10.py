n=int(input("Enter the n value "))
n = 7

for i in range(1, n + 1):
    for j in range(i - 1):
        print(i, end="")
    for j in range(i - 1):
        print("*", end="")

    print()