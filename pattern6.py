number=int(input("enter number : "))
for i in range(number):
    for j in range(i+1):
      if(j%2==0):
         print("1",end='')
      else :
         print("0",end='')   
    print()    