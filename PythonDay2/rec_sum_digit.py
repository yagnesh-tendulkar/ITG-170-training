print("=================== Using recursion finding sum of digit of a number:===============")

def rec_sum_digit(num):
    if num==0:
        return 0
    return (num%10+rec_sum_digit(num//10))




num=int(input("Enter a number : "))
result=rec_sum_digit(num)
print(result)