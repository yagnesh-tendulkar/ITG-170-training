def even_number_sum(num1):
    summ=0
    for i in range(1,num1+1):
        if i%2==0:
            summ=summ+i
    return summ


num1= int(input("Enter a number: "))
print(even_number_sum(num1))