def number_generator():
    for i in range(1, 6):
        yield i

for number in number_generator():
    print(number)