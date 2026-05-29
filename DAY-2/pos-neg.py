# Program to take the number at runtime and check whether the given number  is positive or negative. 
num=int(input("Enter a number:"))
if num>0:
  print(f"{num}is positive")
elif num<0:
  print(f"{num} is negative ")
else:
  print(f"{num}is zero")
