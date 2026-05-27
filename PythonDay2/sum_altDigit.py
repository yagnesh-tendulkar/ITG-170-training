print("=====================:python program to print sum of alternative number :=================")

def SumOfAlterDigit(n):
    summ=0
    for i in n[::2]:
        summ=summ+int(i)
        
    print(summ)



n=input("Enter a number : ")
SumOfAlterDigit(n)