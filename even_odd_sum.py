num=input("enter the number .")
num=int(num)
even_sum=0
odd_sum=0
while(num!=0):
    dig=num%10
    if(dig%2==0):
        even_sum=even_sum+dig
    else :
        odd_sum=odd_sum+dig

    num=num//10   
print(even_sum)
print(odd_sum)     