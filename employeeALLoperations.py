from employeeManagement import EmployeeManagement,UnAuthorized,EmployeeNotFound,DuplicateEmployee
class DisplayOptions:
    @staticmethod
    def operations():
        flag=True
        while(flag):
            print(" "*20,"welcome to employee management")
            print("1.add employee")
            print("2.add Tainee")
            
            print("3.display permanent employees")
            print("4.display all trainees")
            print("5.display all employees")
            print("6.delete  permanent employee")
            print("7.delete trainee")
            print("8.update permanent employee")
            print("9.update traniee")
            print("10.exit")

            ch=int(input("enter your choice : "))
            match(ch):
                case 1:
                    try :
                        EmployeeManagement.add_employee()
                        print("employee added sucessfully")
                    except (UnAuthorized,DuplicateEmployee) as e:
                        print(e.args)
                        continue
                case 2:
                    try :
                        EmployeeManagement.add_trainee()
                        print("trainee added sucessfully")
                    except (UnAuthorized,DuplicateEmployee) as e:
                        print(e.args)
                        continue
                case 3:
                   EmployeeManagement.display_permanent_employee()
                case 4:
                    EmployeeManagement.display_trainee()  
                case 5:
                    EmployeeManagement.display_all_employee()
                case 6:
                    try:
                        EmployeeManagement.delete_employee()
                        print("employee deleted sucessfully")
                    except UnAuthorized as e:
                        print(e.args)
                        continue
                case 7:
                    try:
                        EmployeeManagement.delete_trainee()
                        print("trainee deleted suceesfully")
                    except (EmployeeNotFound ,UnAuthorized) as e:
                        print(e.args)
                        continue
                case 9:
                    try :
                        EmployeeManagement.update_trainee()
                        print("trainne data sucessfully updated")
                    except (UnAuthorized,EmployeeNotFound) as e:
                        print(e.args)
                        continue
                case 8:
                    try:
                        EmployeeManagement.update_permanent_employee()
                        print("employee data update permanently")    
                    except (UnAuthorized ,EmployeeNotFound) as e:
                        print(e.args)
                        continue
                case 10:
                    flag=False
                    
                    print("thank you for visiting")   
                    break         

            print(" do you want to continue : y/n")
            s=input("enter your answer : ")
            if(s.lower()!='y'):
                flag=False
DisplayOptions.operations()                                     

