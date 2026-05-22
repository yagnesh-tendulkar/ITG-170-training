number=int(input(" enter the number "))
dig= int(input("enter digit"))
count=0
while(number!=0):
    rem=number%10;
    if dig==rem:
        count=count+1 
    number=number//10
              
print(count)
