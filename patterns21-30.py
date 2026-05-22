# 21.Program to print prime numbers between m to n.
# m=int(input())
# n=int(input())
# for i in range(m,n+1):
#     if i>1:
#         for j in range(2,(i//2)+1):
#             if i % j==0:
#                 break
#         else:
#             print(i)


# 22.Program to print n prime numbers.
# n=int(input())
# c=1
# num=2
# while c<=n:
#     flag=True
#     for i in range(2,num):
#         if num%i==0:
#             flag=False
#     if flag:
#         print(num,end=" ")
#         c+=1
#     num+=1


# 23.Program to print perfect numbers between m to n.
# m = int(input())
# n = int(input())

# for num in range(m, n + 1):
#     s = 0

#     for i in range(1, num):
#         if num % i == 0:
#             s += i

#     if s == num:
#         print(num, end=" ")


# 24.Program to print n perfect numbers.
# n=int(input())
# c=0
# num=1

# while c<n:
#     s=0
#     for i in range(1,num):
#         if num%i==0:
#             s+=i
#     if s==num:
#         print(s,end=" ")
#         c+=1
#     num +=1


#25.Program to Print Armstrong Number between 1 to 1000.

# for i in range(1,1001):
#     s=0
#     temp=i
#     dig_len=len(str(i))
#     while temp > 0:
#         rem=temp %10
#         s+=rem **dig_len
#         temp //=10
#     if s==i:
#         print(s)

#26 sum of natrural nos 

# def s(n):
#     if n==0:
#         return 0
#     return n+s(n-1)

# print(s(int(input())))


#27 Program to copy all elements of one array into another array.
# a1=[1,2,3,5]
# a2=[]
# a2=a1.copy()
# print(a2)


# 28.Program to find the frequency of each element in the array.
# arr=[1,2,3,7,5,7,2,1,5,7]
# visted=[]
# for i in arr:
#     if i not in visted:
#         c=0
#         for j in arr:
#             if i==j:
#                 c+=1
#         print(i,"=",c)

#         visted.append(i)

# 29.Program to print the duplicate elements of an array.
# arr=[1,2,2,1,3,4,5,6,7,6,5,6]
# v=[]
# for i in arr:
#     if i not in v:
#         v.append(i)
#     else:
#         print(i)


# 30.Program to print the elements of an array in reverse order without sorting.
# arr=[1,3,5,6]
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i])


# 31.Program to find Largest Number and smallest in an Array.
# arr=[4,5,2,7,1]
# ma=arr[0]
# mi=arr[0]
# for i in arr:
#     if ma<i:
#         ma=i
#     elif mi>i:
#         mi=i
# print(ma,mi)
# arr.sort()
# print(arr)



#33.Program to print the sum of all the items of the array.
# arr=map(int,input().split())
# print(sum(arr))

#34.Program to print Odd and Even Numbers from an Array.
arr=[1,4,6,2,3,8]
en=[]
on=[]
for i in arr:
    if i%2==0:
        en.append(i)
    else:
        on.append(i)
print(f"even nums {en} odd nums: {on}")

# 35.Program to check whether a given number is a happy number or not?
n = int(input())

while n != 1 and n != 4:
    s = 0
    while n > 0:
        rem = n % 10
        s += rem ** 2
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
print(s)




# 37.Program to Find the Sum of the Series 1/1+1/2^2+1/3^2+1/4^2+1/5^2.
n = int(input())
s = 0
for i in range(1, n + 1):
    s += 1 / (i ** 2)
print(s)




# 38.Program to Find the Sum of the Series 1/1^0+1/2^1+1/3^2+1/4^3+1/5^4.
n = int(input())
s = 0
for i in range(1, n + 1):
    s += 1 / (i ** (i-1))
print(s)





# 39.Program to Find the Sum of the Series 1/2^0+1/2^1+1/2^2+1/2^3+1/2^4.
n = int(input())
s = 0
for i in range( n ):
    s +=(1/(2**i))
print(s)




# 40.Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
n = int(input())
s = 0
fact=1
for i in range( n ):
    fact *= i
    s += 1 / fact
print(s)




# 41.Program to Find the Sum of the Series 1/1+1/4+1/9+…1/N^2
n = int(input())
s = 0
for i in range(1,n+1):
    
    s += 1 /((i**2)+1)
print(s)



# 42.Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
n = int(input())
s = 0
fact=1
for i in range( n ):
    fact *= i
    s += 1 / fact
print(s)