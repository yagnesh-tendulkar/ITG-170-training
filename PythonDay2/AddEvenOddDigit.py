print("========find the sum of even and odd digit in a number==============")

number=int(input("Enter a Number : "))
number_l=list(map(int,str(number)))
def EvenOdd(number_l):
    even_sum=0
    odd_sum=0
    for i in range(len(number_l)):
        if number_l[i]%2==0:
            even_sum+=number_l[i]
        else:
            odd_sum+=number_l[i]


    return even_sum,odd_sum

e,o = EvenOdd(number_l)
print(f" the even sum is {e} and odd sum is {o} .")