# 11.Given number is perfect number or not
# n=int(input())
# s=0
# for i in range(1,(n//2)+1):
#     if n %i==0:
#         s=s+i
# print("perfect num" if n==s else "not perfect")


# 12.Print the Fibonacci series up to n.

# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# ips=int(input())
# for i in range(ips+1):
#     print(fib(i))

# 13.Find big digit in a number.
# n=int(input())
# l=[int(val) for val in str(n)]
# print(max(l))


# # 14.Program to Find Sum of Digits of a Number using Recursion.
# def s(n):


# 15.Program to print the sum of alternative digits in a given number?
# n=int(input())
# l=[int(val) for val in str(n)]
# s=0
# for i in range(len(l)):
#     if i %2==0:
#         s=s+l[i]
# print(s)

# 16.Program to print the no of occurrences of a digit in a number

# n=int(input())
# d=(input())
# sn=str(n)
# print(sn.count(d))

# 17.Program to whether all digits in a given number are equal or not?
# n=int(input())
# sn=str(n)
# print("equal" if sn.count(sn[-1])==len(sn) else "not wqual")

# 18.Program to add the first and last digit of a given number?
# n=int(input())
# sn=str(n)
# print(int(sn[0])+int(sn[-1]))



# 19.Program to add even and odd digits of a given number?
# n=int(input())
# l=[int(val) for val in str(n)]
# en=od=0
# for i in l:
#     if i%2==0:
#         en +=i
#     else:
#         od +=i
# print(en,od)



# 20.Program to reverse a number?
n=int(input())
rev=0
while n>0:
    
    rev=rev*10+n%10
    n=n//10
print(rev)

