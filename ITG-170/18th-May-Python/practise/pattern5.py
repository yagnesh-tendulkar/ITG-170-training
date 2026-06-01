rows = 5

# Upper part
for i in range(rows):

    # spaces
    for j in range(rows - i - 1):
        print(' ', end='')

    num = 1

    # numbers
    for k in range(i * 2 + 1):
        print(num, end='')

        if k < (i * 2 + 1) // 2:
            num += 1
        else:
            num -= 1

    print()

# Lower part
for i in range(rows - 2, -1, -1):

    # spaces
    for j in range(rows - i - 1):
        print(' ', end='')

    num = 1

    # numbers
    for k in range(i * 2 + 1):
        print(num, end='')

        if k < (i * 2 + 1) // 2:
            num += 1
        else:
            num -= 1

    print()