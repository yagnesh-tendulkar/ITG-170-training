# 1. Sum of elements in a List
lst = [10, 20, 30, 40]
print("1.Sum:", sum(lst))


# 2. Largest Number in the List
lst = [12, 45, 67, 23, 89]
print("2.Largest Number:", max(lst))

#3 Removing the common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
result = []
for i in list1:
    if i not in list2:
        result.append(i)
for i in list2:
    if i not in list1:
        result.append(i)
print("After Removing Common Elements:")
print(result)

# 4. Second-smallest number in a List
lst = [12, 3, 45, 6, 7]
lst.sort()
print("4.Second Smallest:", lst[1])


# 5. Elements in one set but not in another set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("5.Elements not in second set:", set1 - set2)


# 6. Missing numbers between two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("6.Missing in set2:", set1 - set2)
print("Missing in set1:", set2 - set1)


# 7. Pairs whose sum is equal to given value
lst = [1, 2, 3, 4, 5, 6]
target = 7
print("7.Pairs:")
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print((lst[i], lst[j]))


# 8. Two numbers whose product is maximum
lst = [1, 5, 10, 2, 8]
lst.sort()

a = lst[-1]
b = lst[-2]

print("8.Maximum Product Pair:", (a, b))
print("Product:", a * b)


# 9. Maximum and Minimum values in a set
s = {10, 20, 30, 40, 50}

print("9.Maximum:", max(s))
print("Minimum:", min(s))


# 10. Remove an item from a set
s = {1, 2, 3, 4, 5}

s.discard(3)

print("10.After Removing:", s)


# 11. Tuple with different data types
t = ("Varshitha", 21, 95.5, True)

print("11.Tuple:", t)


# 12. Unpack tuple into variables
t = ("Apple", "Banana", "Mango")

a, b, c = t

print("12.Unpacked Values:")
print(a)
print(b)
print(c)


# 13. Find repeated items in a tuple
t = (1, 2, 3, 2, 4, 5, 1)

print("13.Repeated Items:")
for i in set(t):
    if t.count(i) > 1:
        print(i)


# 14. Reverse a tuple
t = (1, 2, 3, 4, 5)

print("14.Reversed Tuple:", t[::-1])


# 15. Replace last value in tuples
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result = [i[:-1] + (100,) for i in lst]

print("15.After Replacing:", result)


# 16. Convert tuple into integer
t = (1, 2, 3)

num = int("".join(map(str, t)))

print("16.Integer:", num)


# 17. Sum of elements of each tuple
lst = [(1, 2), (2, 3), (3, 4)]

result = [sum(i) for i in lst]

print("17.Sum of Tuples:", result)


# 18. Dictionary with squares
d = {}

for i in range(1, 11):
    d[i] = i * i

print("18.Dictionary:", d)


# 19. Combine two dictionaries
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = Counter(d1) + Counter(d2)

print("19.Combined Dictionary:", result)


# 20. Convert lists to nested dictionary
ids = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
marks = [85, 98, 89, 92]

result = []

for i in range(len(ids)):
    result.append({ids[i]: {names[i]: marks[i]}})

print("20.Nested Dictionary:")
print(result)


# 21. Convert dictionary into list of lists
d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

result = [[k, v] for k, v in d.items()]

print("21.List of Lists:")
print(result)


# 22. Get key, value and item in dictionary
d = {'a': 10, 'b': 20, 'c': 30}

print("22.Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())


# 23. Maximum and minimum values of dictionary
d = {'a': 10, 'b': 50, 'c': 5}

print("23.Maximum Value:", max(d.values()))
print("Minimum Value:", min(d.values()))