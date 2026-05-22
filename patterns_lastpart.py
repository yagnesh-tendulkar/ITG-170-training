#  1
#  212
# 32123
# 4321234
# n=int(input())
# for i in range(1,n+1):
#     for sp in range(1,(n-i)+1):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     for inc in range(2,i+1):
#         print(inc,end=" ")
#     print()


# 1 2 3 4
#  2 3 4
#  3 4
#  4
#  3 4
#  2 3 4
# #  1 2 3 4
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for num in range(i,n+1):
#         print(num,end=" ")
#     print()
# for i in range(1,n):
#     for sp in range(1,n-i):
#         print(" ",end=" ")
#     for num in range(n-i,n+1):
#         print(num,end=" ")
#     print()

# 1
#  1*2
#  1*2*3
#  1*2*3*4
#  1*2*3*4*5
#  1*2*3*4*5*6
#  1*2*3*4*5*6*7

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==i:
#             print(j,end="")
#         else:
#             print(f"{j}*",end="")
#     print()

# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+i),end=" ")
#     print()




# A B C D E F G
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A 



# n=int(input())
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()




# 1
# *2*
# **3**
# ***4***
# ****5****
# *****6*****
# ******7******

# n=int(input())
# for i in range(1,n+1):
#     print((i-1)*"*",i,(i-1)*"*",sep="")  
