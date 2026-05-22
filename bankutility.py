from bank import Account,NegativeNumberError,InsufficentAmount
class InvalidCrendials(Exception):
     def __init__(self,msg):
        super().__init__(msg)  
class BankUtility:
    @staticmethod
    def acess():
       
        attempt=3
        while(attempt!=0):
            acc=input("enter your account no : ")
            pas=input("enter password : ")
            if  Account.login(acc,pas):
                return True
                break
            else :
                attempt=attempt-1
                print("invalid credentials")
                print("you have left {} more try".format(attempt))
        return False        
        
            
    @staticmethod
    def operation():
        flag=BankUtility.acess()
        try:
            if flag==False:
                raise InvalidCrendials("you are out of tries")
        except InvalidCrendials as e:
             print(e.args)    
        if flag:
         while(flag):
            print("enter your choices from below")
            print("1.deposit")
            print("2.withdraw")
            print("3.amount")
            print("4.exit")
            choice=int(input("enter your choice"))
            match(choice):
                case 1:
                    amount=int(input("enter amount"))
                    try:
                         Account.deposit(amount)
                    except NegativeNumberError as e:
                        print(e.args)  
                        continue   
                case 2:
                    try :
                        amount=int(input("enter amount"))
                        Account.withdrwal(amount) 
                    except   (InsufficentAmount,NegativeNumberError) as e:
                        print(e.args)  
                        continue

                case 3:
                    acountno=input("enter account")
                    try:
                     Account.showdetalils(acountno)
                    except InvalidCrendials as e:
                        print(e.args) 
                        continue
                case 4:
                    flag=False    
            print("do you want to continue ? y\n")
            ch=input("enter choice : ")
            if ch.lower()!='y': 
                flag=False   
        print("thank you for your time")            
BankUtility.operation()                          
                   


                    

    