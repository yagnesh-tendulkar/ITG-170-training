row=int(input("enter the rows ."))
spaces=row-1;
stars=1
for i in range(1,row*2):
 for j in range(spaces):
  print("",end="  ")
 for k in range(stars):
  print("* ",end="")
 if(i<row):
   spaces=spaces-1
   stars=stars+2
 else :
   spaces=spaces+1
   stars=stars-2 
 print()    
