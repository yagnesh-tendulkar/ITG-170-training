print("==========Program to find first ansd last digit of a number===========")
num=int(input("Enter a Number : "))
num_l=list(map(int,str(num)))
count=0

print(f"first digit of the number {num_l[0]} last digit of the number is {num_l[-1]}")