def NumberofNumber(*args):
    """
    this is a NumberofNumber funtion used to make any number of inputs and uses 
    *args arguments to pass it and sum all this in this funtion and finally returns it 
    
    """
    total=0
    for i in range(len(args)):
        total+=args[i]
    
    return f"Total sum  is {total}"



print(NumberofNumber(5,6,7,8,9,1,2,3))