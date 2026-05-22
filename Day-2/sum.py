n = int(input("Enter the value of n: "))

sum_even = 0

for i in range(2, n + 1, 2):
    sum_even += i

print("Sum of all even numbers from 1 to", n, "is:", sum_even)
