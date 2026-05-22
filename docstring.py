def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
sum(1,2,3,4,5)    
""" function sum has *args parameter which takes multiple arguments and return sum of their values"""