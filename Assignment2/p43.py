# 43.Write a program to display pattern
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()

# =============================
# #    *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
# #    *
# n=5
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()

# 1
# 12 
# 123
# 1234
# 12345
# m=5
# for i in range(1,m+1):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()
# =====================
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# m=5
# s=0
# for i in range(1,m+1):
#     for j in range(1,i):
#         s= s+1
#         print(s,end=" ")
#     print()
# =========================
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
# n=5
# for i in range(n):
#     for j in range(1,n-i+1):
#         print(j,end=" ")
#     print()
# =============================
# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1 
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(n-i,end=" ")
#     print()
# ============================

# 5 
# 5 4 
# 5 4 3 
# 5 4 3 2 
# 5 4 3 2 1 
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(n-j,end=" ")
        
#     print()
# ==============================
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 
# n=5
# for i in range(n):
#     for j in range(i+1,0,-1):
#         print(j,end=" ")
        
#     print()
# ================================
# n=5
# for i in range(n):
#     # k=0
#     for j in range(i+1):
#         if (i+j) % 2 == 0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
        
#     print()
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 
    
# A
# AB
# ABC
# ABCD
# ABCDE
# ABCDEF
# n=5

# for i in range(n):
#     ch = ord('A')
#     for j in range(i+1):
#         print(chr(ch),end=" ")
#         ch = ch + 1
#     print()
# =================
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# n=5
# ch = ord('A')
# for i in range(n):
    
#     for j in range(i+1):
#         print(chr(ch),end=" ")
#         ch = ch + 1
#     print()
# ============
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

# n=5
# for i in range(n):
#     ch = ord('A')
#     for j in range(n-i,0,-1):
#         print(chr(ch),end=" ")
#         ch = ch+1
#     print()

# ******1
# *****12
# ****123
# ***1234
# **12345
# *123456
# 1234567
n=7

# for i in range(1,n+1):
#     for j in range(n-i):
#         print("* ",end="")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()git remote add origin https://github.com/roshinipriyankavemavarapu04/Training_assess.git
# =====================
# 1
# 1*2
# 1*2*3
# 1*2*3*4
# 1*2*3*4*5
# 1*2*3*4*5*6
# 1*2*3*4*5*6*7
# n=5
# s=1
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="* ")
        
#     print()

# 1
# *2*
# **3**
# ***4***
# ****5****
# *****6*****
# ******7******
# n=7
# for i in range(1,n+1):
#     for j in range(i-1):
#         print("*",end=" ")
#     print(i,end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()
# =============
# 1
# *2*
# **3**
# ***4***
# ****5****
# *****6*****
# ******7******
# n = 7
# for i in range(1, n + 1):
#     # 1. Print stars BEFORE the number (only if i > 1)
#     for j in range(i - 1):
#         print("*", end="")
    
#     # 2. Print the number
#     print(i, end="")
    
#     # 3. Print stars AFTER the number (only if i > 1)
#     for k in range(i - 1):
#         print("*", end="")
    
#     # 4. Move to the next line
#     print()
# ===========================
#    1
#   212
#  32123
# 4321234
# n=4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         print(k,end=" ")
#     for s in range(2,i+1):
#         print(s,end=" ")
#     print()
