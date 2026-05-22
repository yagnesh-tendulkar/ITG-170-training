def number_generator():
    for i in range(1, 6):
        yield i

gen = number_generator()

for num in gen:
    print(num)