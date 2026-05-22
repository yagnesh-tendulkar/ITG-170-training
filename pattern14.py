row=int(input("enter number of rows"))
for i in range(1,row+1):
    
    for k in range(row-i):
        print(" ",end=" ")
        num=i
    for j in range(1,i*2):
       print(num,end=" ") 
       if j<i:
           num=num-1
       else :
           num=num+1
    print()       
              
