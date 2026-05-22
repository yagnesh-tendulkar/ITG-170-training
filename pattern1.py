#pyramid pattern
number=int(input("enter number of row ."))
for i in range(number):
   for j in range(number-i):
     print("",end=" ")
   for k in range(i+1):
      print("*",end=' ')
   print()   

