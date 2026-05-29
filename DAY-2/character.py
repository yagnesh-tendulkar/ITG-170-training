# Set the number of rows (6 rows for A through F)
rows = 6

for i in range(1, rows + 1):
    # Inner loop to handle the letters in each row
    for j in range(i):
        # 65 is 'A', 66 is 'B', and so on...
        print(chr(65 + j), end=" ")
    # New line after each row
    print()