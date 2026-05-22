# Write a generator that yields even numbers up to 10.
def even_gen():
    for i in range(2, 11, 2):
        yield i

g = even_gen()
for num in g:
    print(num)



