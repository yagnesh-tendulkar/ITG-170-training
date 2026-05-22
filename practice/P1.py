"""
*
**
***
****
*****
for i in range (1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
    or
for i in range (1,6):
    print("*"*i)
    or
[print("*"*i) for i in range (1,6)]"""
"""
*
***
*****
*******
*********
*******
*****
***
*
for i in range (1,10,2):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
for i in range (7,0,-2):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
    or
for i in range (1,10,2):
    print("*"*i)
for i in range (7,0,-2):
    print("*"*i)
    or
[print("*"*i)for i in range(1,10,2)]
[print("*"*i)for i in range(7,0,-2)]
    """
"""
   *
  **
  ***
 ****
 *****
******

for i in range(1,7):
    print(" "*(6-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
    """
"""  
     *
    **
   ***
  ****
 *****
******

for i in range(1,7):
    print(" "*(6-i),end="")
    print("*"*i,end=" ")
    print("")
    or
for i in range(1,7):
    print(" "*(6-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")
    """
"""
******
*****
 ****
 ***
  **
  *

for i in range(6,0,-1):
    print(" "*(6-i),end="")
    for j in range(1,i+1):
        print("*",end=(" "))
    print("")
    """
"""
******
 *****
  ****
   ***
    **
     *

for i in range(6,0,-1):
    print(" "*(6-i),end="")
    for j in range(1,i+1):
        print("*",end=(""))
    print("")
    or
for i in range(6,0,-1):
    print(" "*(6-i),end="")
    print("*"*i,end=" ")
    print("")
    """
"""
    *
   ***
  *****
 *******
*********

for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    for k in range(2,i+1):
        print("*",end="")
    print("")
  or
for i in range(1,10,2):
    print(" "*((9-i)//2)+"*"*i)
      """
"""
1
12
123
1234
12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("")
    or

[print("".join(str(j) for j in range(1,i+1))) for i in range(1,6)]
or
s = ""

for i in range(1,6):
    s += str(i)
    print(s)
        """
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

n=1
for i in range(1,6):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print("")
    or
n=1
for i in range(1,6):
    for j in range(i):
        print(n,end=" ")
        n=n+1
    print("")
"""
"""
5
54
543
5432
54321

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print("")
    """
"""
54321
5432
543
54
5
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print("")
"""
"""
1
21
321
4321
54321

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    print("")
    """
"""
1
10
101
1010
10101

for i in range(1,6):
    for j in range(i):
        if(j%2==0):
            print("1",end="")
        else:
            print("0",end="")
    print("")
"""
"""
1
00
111
0000
11111
for i in range(1,6):
    for j in range(i):
        if(i%2==0):
            print("0",end="")
        else:
            print("1",end="")
    print("")
"""
"""
   1
  212
 32123
4321234

for i in range(1,5):
    print(" "*(4-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print("")
    """
"""
1 2 3 4
 2 3 4
  3 4
   4
  3 4
 2 3 4
1 2 3 4

for i in range(1,5):
    print(" "*(i-1),end="")
    for j in range(i,5):
        print(j,end=" ")
    print("")
for i in range(4,0,-1):
    print(" "*(i-1),end="")
    for j in range(i,5):
        print(j,end=" ")
    print("")
"""
"""
15
14 13
12 11 10
9 8 7 6
5 4 3 2 1

n=15
for i in range(1,6):
    for j in range(1,i+1):
        print(n,end=" ")
        n-=1
    print("")
    """
"""
15 14 13 12 11
10 9 8 7 
6 5 4
3 2
1

n=15
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(n,end=" ")
        n=n-1
    print("")
    """
"""
1
1*2
1*2*3
1*2*3*4
1*2*3*4*5
1*2*3*4*5*6

for i in range(1,7):
    for j in range(1,i+1):
        if j==i:
            print(j,end="")
        else:
            print(j,end="*")
    print("")
    """
"""
A
A B
A B C
A B C D
A B C D E

for i in range(1,7):
    for j in range(0,i):
        print(chr(65+j),end=" ")
    print("")
    """
"""
ABCDEF
ABCDE
ABCD
ABC
AB
A

for i in range(6,0,-1):
    for j in range(0,i):
        print(chr(65+j),end=" ")
    print("")
    """
"""
1
*2*
**3**
***4***
****5****
*****6*****

for i in range(1,7):
    print("*"*(i-1),i,"*"*(i-1))
    print("")
    """
"""
*****1
****12
***123
**1234
*12345
123456

for i in range(1,7):
    print("*"*(6-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print("")
"""
"""
    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1
for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print("")
for i in range(4,0,-1):
    print(" "*(5-i),end="")
    for j in range(1,i):
        print(j,end="")
    for j in range(i,0,-1):
        print(j,end="")
    print("")"""
# s1 = input("Enter first sentence: ").split()
# s2 = input("Enter second sentence: ").split()

# common_words = [x for x in s1 if x==x in s2]

# print("Common words in reverse characters:")

# for word in common_words:
#     print(word[::-1])
