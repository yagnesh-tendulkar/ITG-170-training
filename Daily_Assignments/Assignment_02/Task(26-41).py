# Function to copy elements of one array into another
def copy_array():
    size = int(input("Enter size of array: "))
    array1 = []
    print("Enter array elements:")
    for i in range(size):
        value = int(input())
        array1.append(value)
    array2 = array1.copy()
    print("Copied Array:", array2)

# Function to find frequency of each element
def frequency_of_elements():
    size = int(input("Enter size of array: "))
    array = []
    print("Enter array elements:")
    for i in range(size):
        value = int(input())
        array.append(value)
    visited = []
    for i in range(size):
        if array[i] in visited:
            continue
        count = 0
        for j in range(size):
            if array[i] == array[j]:
                count += 1
        visited.append(array[i])
        print(array[i], "occurs", count, "times")

# Function to print duplicate elements
def duplicate_elements():
    size = int(input("Enter size of array: "))
    array = []
    print("Enter array elements:")
    for i in range(size):
        value = int(input())
        array.append(value)
    print("Duplicate Elements:")
    duplicates = []
    for i in range(size):
        for j in range(i + 1, size):
            if array[i] == array[j] and array[i] not in duplicates:
                duplicates.append(array[i])
                print(array[i])

# Function to print array in reverse order
def reverse_array():
    size = int(input("Enter size of array: "))
    array = []
    print("Enter array elements:")
    for i in range(size):
        value = int(input())
        array.append(value)
    print("Array in Reverse Order:")
    for i in range(size - 1, -1, -1):
        print(array[i], end=" ")

# Function to find largest and smallest element
def largest_and_smallest():
    size = int(input("Enter size of array: "))
    array = []
    print("Enter array elements:")
    for i in range(size):
        value = int(input())
        array.append(value)
    largest = array[0]
    smallest = array[0]
    for value in array:
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
    print("Largest Number =", largest)
    print("Smallest Number =", smallest)

# Function to sort array in descending order
def descending_order():
    size = int(input("Enter size of array: "))
    array = []
    print("Enter array elements:")
    for i in range(size):
        value = int(input())
        array.append(value)
    array.sort(reverse=True)
    print("Descending Order:", array)

# Function to print sum of array elements
def sum_of_array():
    size = int(input("Enter size of array: "))
    array = []
    print("Enter array elements:")
    for i in range(size):
        value = int(input())
        array.append(value)
    total_sum = 0
    for value in array:
        total_sum += value
    print("Sum of Array Elements =", total_sum)

# Function to print odd and even numbers from array
def odd_even_array():
    size = int(input("Enter size of array: "))
    array = []
    print("Enter array elements:")
    for i in range(size):
        value = int(input())
        array.append(value)
    print("Even Numbers:")
    for value in array:
        if value % 2 == 0:
            print(value, end=" ")
    print("\nOdd Numbers:")
    for value in array:
        if value % 2 != 0:
            print(value, end=" ")

# Function to check happy number
def happy_number():
    number = int(input("Enter a number: "))
    original = number
    while number != 1 and number != 4:
        total = 0
        while number > 0:
            digit = number % 10
            total += digit * digit
            number //= 10
        number = total
    if number == 1:
        print(original, "is a Happy Number")
    else:
        print(original, "is Not a Happy Number")

# Function to find sum of series 1 + 1/2 + 1/3 + ... + 1/N
def series1():
    n = int(input("Enter value of N: "))
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    print("Sum =", total)

# Function to find sum of series 1/1^2 + 1/2^2 + ...
def series2():
    n = int(input("Enter value of N: "))
    total = 0
    for i in range(1, n + 1):
        total += 1 / (i ** 2)
    print("Sum =", total)

# Function to find sum of series 1/1^0 + 1/2^1 + ...
def series3():
    n = int(input("Enter value of N: "))
    total = 0
    power = 0
    for i in range(1, n + 1):
        total += 1 / (i ** power)
        power += 1
    print("Sum =", total)

# Function to find sum of series 1/2^0 + 1/2^1 + ...
def series4():
    n = int(input("Enter value of N: "))
    total = 0
    for i in range(n):
        total += 1 / (2 ** i)
    print("Sum =", total)

# Function to find factorial
def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

# Function to find sum of factorial series
def factorial_series():
    n = int(input("Enter value of N: "))
    total = 0
    for i in range(1, n + 1):
        total += 1 / factorial(i)
    print("Sum =", total)

print("26. Copy Array")
print("27. Frequency of Elements")
print("28. Duplicate Elements")
print("29. Reverse Array")
print("30. Largest and Smallest in Array")
print("31. Descending Order of Array")
print("32. Sum of Array Elements")
print("33. Odd and Even Numbers from Array")
print("34. Happy Number")
print("35. Sum of Series 1 + 1/2 + ... + 1/N")
print("36. Sum of Series 1/1^2 + 1/2^2 + ...")
print("37. Sum of Series 1/1^0 + 1/2^1 + ...")
print("38. Sum of Series 1/2^0 + 1/2^1 + ...")
print("39. Sum of Series 1/1! + 1/2! + ...")
print("40. Sum of Series 1/1^2 + 1/2^2 + ...")
print("41. Sum of Series 1/1! + 1/2! + ...")

choice = int(input("\nEnter your choice: "))

if choice == 26:
    copy_array()
elif choice == 27:
    frequency_of_elements()
elif choice == 28:
    duplicate_elements()
elif choice == 29:
    reverse_array()
elif choice == 30:
    largest_and_smallest()
elif choice == 31:
    descending_order()
elif choice == 32:
    sum_of_array()
elif choice == 33:
    odd_even_array()
elif choice == 34:
    happy_number()
elif choice == 35:
    series1()
elif choice == 36:
    series2()
elif choice == 37:
    series3()
elif choice == 38:
    series4()
elif choice == 39:
    factorial_series()
elif choice == 40:
    series2()
elif choice == 41:
    factorial_series()
else:
    print("Invalid Choice")