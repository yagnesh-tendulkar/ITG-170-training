# 31.Program to find Largest Number and smallest in an Array.
arr = [10, 25, 5, 80, 45]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest Number :", largest)
print("Smallest Number:", smallest)

# 32.Program to sort the elements of an array in descending order.

arr = [40, 10, 50, 20, 30]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Array in descending order:")
print(arr)




# 33.Program to print the sum of all the items of the array.
arr = [10, 20, 30, 40, 50]

s = 0

for i in arr:
    s += i

print("Sum of array elements:", s)



# 34.Program to print Odd and Even Numbers from an Array.
arr = [10, 15, 22, 7, 18, 31]

print("Even Numbers:")
for i in arr:
    if i % 2 == 0:
        print(i, end=" ")

print("Odd Numbers:")
for i in arr:
    if i % 2 != 0:
        print(i, end=" ")




# 35.Program to check whether a given number is a happy number or not?
n = int(input())

while n != 1 and n != 4:
    s = 0

    while n > 0:
        rem = n % 10
        s += rem * rem
        n //= 10

    n = s

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")





# 36.Program to Find the Sum of the Series 1/1+1/2+1/3+…1/N.
n = int(input())

s = 0

for i in range(1, n + 1):
    s += 1 / i

print("Sum =", s)





# 37.Program to Find the Sum of the Series 1/1+1/2^2+1/3^2+1/4^2+1/5^2.
n = int(input())

s = 0

for i in range(1, n + 1):
    s += 1 / (i ** 2)

print("Sum =", s)



#40
n = int(input())

s = 0
fact = 1

for i in range(1, n + 1):
    fact *= i
    s += 1 / fact

print("Sum =", s)

# 41.Program to Find the Sum of the Series 1/1+1/4+1/9+…1/N^2

n = int(input())

s = 0

for i in range(1, n + 1):
    s += 1 / (i ** 2)

print("Sum =", s)




#45
class Student:
    def __init__(self):
        self.name = "Vaishnavi"   # public variable

obj = Student()

print(obj.name)




class Student:
    def __init__(self):
        self.__marks = 95   # private variable

obj = Student()

# print(obj.__marks)   # Error





class Parent:
    def __init__(self):
        self._salary = 50000   # protected variable

class Child(Parent):
    def display(self):
        print(self._salary)

obj = Child()
obj.display()