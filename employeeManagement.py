from Employye import employee
class UnAuthorized(Exception):
    pass
class EmployeeNotFound(Exception):
    pass
class DuplicateEmployee(Exception):
    pass

class EmployeeManagement:
    permanentMembers=[employee("harsha","trainer","2345"),employee("saradhi","trainer","5673"),employee("ignesh","trainer","3456"),employee("rani priyanka","trainer","9090"),employee("vasudev","hr","3245"),employee("purnima","hr","7834")]
    Trainne=[employee("rudra","trainee","2460"),employee("mahesh","tainee","4260"),employee("amrut","trainee","9938")]
    @staticmethod
    def __add_employee_details():
        name=input("enter name : ").strip()
        role=input (" enter role : ").strip()
        eid=input("enter eid : ")
        duplicate=False
        for i in EmployeeManagement.permanentMembers:
            if(i.getId().lower()==eid.lower()):
                duplicate=True
                break
        for j in EmployeeManagement.Trainne:
            if(j.getId().lower()==eid.lower()):
                duplicate=True 
                break 
        if(duplicate):
                raise DuplicateEmployee("employee having this eid already exists")
        else :
                return employee(name,role,eid)     
      

    @staticmethod
    def add_employee():
        eid=input("enter eid : ").strip()
        acess=False
        role=input("enter youtr role ").strip()
        for i in EmployeeManagement.permanentMembers:
            if(i.getId()==eid and i.getRole().lower()==role.lower() and i.getRole().lower()=="hr"):
              acess=True
              break
        if(acess):
            EmployeeManagement.permanentMembers.append(EmployeeManagement.__add_employee_details()) 
        else :
            raise UnAuthorized("you are not authorized to do it")       
    @staticmethod        
    def add_trainee() :
        eid=input("enter eid : ")
        role=input("enter youtr role ")
        acess=False
        for i in EmployeeManagement.permanentMembers:
            if(i.getId()==eid and i.getRole().lower()==role.lower() and i.getRole().lower()=="hr"):
                acess=True
                break
        if(acess):
            EmployeeManagement.Trainne.append(EmployeeManagement.__add_employee_details())       
        else:
                raise UnAuthorized("you are not authorize to add employees ")
    @staticmethod
    def display_all_employee():
        for i in EmployeeManagement.permanentMembers:
            i.all_details()
        for j in EmployeeManagement.Trainne:
            j.all_details()  
    @staticmethod        
    def display_trainee():
           for j in EmployeeManagement.Trainne:
            j.all_details() 
    @staticmethod        
    def display_permanent_employee():
                 for i in EmployeeManagement.permanentMembers:
                   i.all_details()
    @staticmethod
    def delete_employee():
        eid=input("enter eid : ")
        role=input("enter youtr role ")
        acess=False
        for i in EmployeeManagement.permanentMembers:
            if(i.getId()==eid and i.getRole().lower()==role.lower() and i.getRole().lower()=="hr"):
                acess=True
                break
            
        if(acess):
            id=input("enter employee id for delete")
            obj=None
            for i in EmployeeManagement.permanentMembers:
                    if(id.lower()==i.getId()):
                        obj=i
            if(obj!=None):
                   EmployeeManagement.permanentMembers.remove(obj)
            else:
                    raise EmployeeNotFound("employee with this id is not present")  
        else :
            raise UnAuthorized(" you are not authorize to do deletion")      
                                        
               
                
          
    @staticmethod        
    def delete_trainee():

        eid=input("enter eid : ")
        role=input("enter youtr role ")
        acess=False
        for i in EmployeeManagement.permanentMembers:
            if(i.getId()==eid and i.getRole().lower()==role.lower()  and i.getRole().lower()=="hr"):
                acess=True
                break
        if(acess):
                id=input("enter employee id for delete")
                obj=None
                for i in EmployeeManagement.Trainne:
                    if(id.lower()==i.getId()):
                        obj=i
                if(obj!=None):
                   EmployeeManagement.Trainne.remove(obj)
                else:
                    raise EmployeeNotFound("employee with this id is not present")
                                        
               
                
        else:
                raise UnAuthorized("you are not authorize to add role")
                       
    def update_permanent_employee():
        eid=input("enter eid : ")
        role=input("enter youtr role ")
        acess=False
        for i in EmployeeManagement.permanentMembers:
            if i.getId()==eid and i.getRole().lower()==role.lower() and i.getRole()=="hr":
                acess=True
                break
        if(acess):
             eid=input("enter eid for updation: ")
             obj=None
             for i in EmployeeManagement.permanentMembers:
                  if i.getId().lower()==eid:
                       obj=i
                       break
             if(obj!=None):
                  print("update details")
                  print("1.update Name")
                  print("2.update role") 
                  print("3.update name and role")
                  flag=True
                  ch=int(input("enter your choice"))
                  match(ch):
                    case 1:
                       name=input("enter new name : ")
                       obj.setName(name)
                       print("name updated sucessfully")
                    case 3:
                         name=input("enter new name : ")
                         obj.setName(name)  
                         role=input("enter new role")
                         obj.setRole(role)
                         print("role and name updated sucessfully")
                    case 2:
                           role=input("enter new role")
                           obj.setRole(role)                
             else:
                  raise EmployeeNotFound(" employee with this is not present")       
             
    @staticmethod
    def update_trainee():
        eid=input("enter eid : ")
        role=input("enter youtr role ")
        acess=False
        for i in EmployeeManagement.permanentMembers:
            if i.getId()==eid and i.getRole().lower()==role.lower() and (i.getRole().lower()=="trainer" or i.getRole().lower()=="hr"):
                acess=True
                break
        if(acess):
             eid=input("enter eid for updation: ")
             obj=None
             
             for i in EmployeeManagement.Trainne:
                  if i.getId().lower()==eid:
                       obj=i
                       break
             if(obj!=None):
                  print("update details")
                  print("1.update Name")
                  print("2.update role") 
                  print("3.update name and role")
                  flag=True
                  ch=int(input("enter your choice"))
                  match(ch):
                    case 1:
                       name=input("enter new name : ")
                       obj.setName(name)
                       print("name updated sucessfully")
                    case 3:
                         name=input("enter new name : ")
                         obj.setName(name)  
                         role=input("enter new role")
                         obj.setRole(role)
                         
                         print("role and name updated sucessfully")
                    case 2:
                           role=input("enter new role")
                           obj.setRole(role)                
             else:
                  raise EmployeeNotFound(" employee with this is not present")   
        else :
             raise UnAuthorized("yopu are not authorized to do updation")
                   
                  
                 

   
                               

               


                                                                                                                                                                                                                                                                    