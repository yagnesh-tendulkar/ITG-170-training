class Overload:

    def add(self,*args):
        if(len(args)==1):
            print("Added number is : ",args[0])
        elif(len(args)==2):
            print("Added number is :",args[0]+args[1])
        elif(len(args)==3):
            print("Added number is :",args[0]+args[1]+args[2])
        else:
            print("Error")

    
ov1=Overload()
ov1.add(4,5)
ov1.add(1,5,9)
ov1.add(3)