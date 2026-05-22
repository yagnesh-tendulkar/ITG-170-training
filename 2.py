# Write a program using any() to check if any number in a list is negative.
l=[1,2,5,6,-8,7,5,-1,29,45]
print(any(x<0 for x in l))


# Write a program using all() to check if all numbers are positive.
print()


# Generator function
# Create a generator that prints numbers from 1 to 5.

def gen():
    for i in range(1, 6):
        yield i
g = gen()
for value in g:
    print(value)



# interest.py

def simp_intr(p, t, r):
    si = (p * t * r) / 100
    return si

