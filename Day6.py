# 1. Create a module 
def add(a, b):
    return a + b

result = add(10, 20)

print("Addition:", result)


# 2. Using any() to check if any number is negative

numbers = [10, 5, -2, 8]

check_negative = any(num < 0 for num in numbers)

print("Any negative number:", check_negative)



# 3. Using all() to check if all numbers are positive

nums = [2, 5, 8, 10]

check_positive = all(num > 0 for num in nums)

print("All numbers are positive:", check_positive)



# 4. Generator that prints numbers from 1 to 5

def number_generator():
    for i in range(1, 6):
        yield i

print("\nNumbers from generator:")
for value in number_generator():
    print(value)



# 5. Using with statement to open a file and print contents


with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)

# 6. Module for Simple Interest

def simple_interest(p, t, r):
    return (p * t * r) / 100

si = simple_interest(10000, 2, 5)

print("Simple Interest:", si)


# 7. Create an iterator for a list of numbers

numbers_list = [1, 2, 3, 4, 5]

iterator_obj = iter(numbers_list)

print("\nIterator Output:")
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))



# 8. Generator that yields even numbers up to 10

def even_numbers():
    for i in range(2, 11, 2):
        yield i


print("\nEven Numbers:")
for num in even_numbers():
    print(num)



# 9. Use any()
values = [20, 45, 150, 60]

greater_than_100 = any(num > 100 for num in values)

print("\nContains number greater than 100:", greater_than_100)