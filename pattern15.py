#pyramid pattern
#pyramid pattern
number=int(input("enter number of row ."))
for i in range(number+1):
   for j in range(number-i):
     print("",end=" ")
   for k in range(i):
      print("*",end=' ')
   print()   

