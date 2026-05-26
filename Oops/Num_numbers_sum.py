def sum(*number):
    """ Returns the sum of all the arguments that you have provided """
    total=0
    for i in number:
        total+=i
    print("Total sum : ",total)
sum(6,34,5,7,9,)