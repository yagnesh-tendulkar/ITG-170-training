rows = int(input('Enter a number: '))
for i in range(rows):
    print(' '*(rows-i)+'* '*i)
for i in range(rows,0,-1):
    print(' '*(rows-i)+'* '*i)
