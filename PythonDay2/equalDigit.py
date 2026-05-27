print("==========Program to find all number are equal or not===========")
num=int(input("Enter a Number : "))
num_l=list(map(int,str(num)))
count=0

for i in range(1,len(num_l)):
    if num_l[i]!=num_l[i-1]:
        print("All digits not equal !")
        break
    
    else:
        count+=1

if count==len(num_l)-1:
    print("All digits are equal")
 
