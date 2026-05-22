arr = [1, 2, 2, 3, 4, 1, 2, 5]

frequency = {}

for element in arr:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("Frequency of each element:")

for key, value in frequency.items():
    print(key, "->", value)
