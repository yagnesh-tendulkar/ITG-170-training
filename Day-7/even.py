def even_numbers():
    for i in range(2, 11, 2):
        yield i

ev = even_numbers()

for num in even_numbers():
    print(num)








