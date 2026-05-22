#Program to add even and odd digits of a given number?
num=int(input("Enter a number:"))
even_sum=0
odd_sum=0
while num>0:
    rem=num%10
    
    if rem%2!=0:
        odd_sum+=rem
    else:
        even_sum+=rem
    num=num//10
print("sum of odd digits:",odd_sum)
print("sum of even digts:",even_sum)