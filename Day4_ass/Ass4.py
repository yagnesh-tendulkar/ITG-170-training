#Create a function that accepts any number of numbers and returns their sum.
def total(*numbers):
    return sum(numbers)
print("sum of numbers:",total(1,2,3,4,5))