from entity.HR import HR
from entity.Trainer import Trainer
from entity.Trainee import Trainee
from exceptions.InvalidAuthorizationException import InvalidAuthorizationException
from exceptions.InvalidCredentialsException import InvalidCredentialsException
from exceptions.EmployeeNotExistException import EmployeeNotExistException
from exceptions.OutOfMemoryException import OutOfMemoryException

class EmployeeService:
    hr1 = HR(101, 'Priya', 'HR', 28, 40000)
    hr2 = HR(102, 'Rahul', 'HR', 30, 45000)

    # Trainers
    trainer1 = Trainer(201, 'Kiran', 'Trainer', 35, 70000)
    trainer2 = Trainer(202, 'Anjali', 'Trainer', 32, 65000)

    # Trainees
    trainee1 = Trainee(301, 'Aman', 'Trainee', 21, 15000)
    trainee2 = Trainee(302, 'Sneha', 'Trainee', 22, 15000)
    trainee3 = Trainee(303, 'Ravi', 'Trainee', 23, 15000)
    trainee4 = Trainee(304, 'Divya', 'Trainee', 20, 15000)
    trainee5 = Trainee(305, 'Arjun', 'Trainee', 24, 15000)
    trainee6 = Trainee(306, 'Meena', 'Trainee', 22, 15000)
    employees=[hr1,hr2,trainer1,trainer2,trainee1,trainee2,trainee3,trainee4,trainee5,trainee6]

    def addEmployee(self, employee):

        role = input('Enter your designation: ').lower()
        name = input('Enter your name: ').lower()

        tempRole = None

        for e in self.employees:

            if e.name.lower() == name:

                tempRole = e.role.lower()

                if tempRole == 'hr' or tempRole == 'trainer':
                    self.employees.append(employee)

                    return f'Employee record saved successfully with {employee.id}'

        raise InvalidAuthorizationException('Contact your HR for creating employee')

    def deleteEmployee(self, id):

        role = input('Enter your designation: ').lower()
        name = input('Enter your name: ').lower()

        for e in self.employees:

            if e.name.lower() == name:

                tempRole = e.role.lower()

                if tempRole == 'hr' or tempRole == 'trainer':

                    for t in self.employees:

                        if t.id == id:
                            self.employees.remove(t)

                            print('Employee record deleted successfully!!!')
                            return

                    print('Employee not found')
                    return

                else:
                    raise InvalidAuthorizationException('Contact your HR for deleting employee')

    def getAllTrainees(self):
        count=0
        for e in self.employees:
            if e.role.lower()=='trainee':
                print(e)
                count+=1
        if(count==0):
            raise EmployeeNotExistException('There are no trainees now, please try later!!')


    def updateEmployee(self,id,employee):
        count=0
        for e in range(0,len(self.employees)):
            if self.employees[e].id==id:
                count+=1
                self.employees[e]=employee
        if count==0:
            raise EmployeeNotExistException('Employee does not exist in Database')
        else:
            print('Employee record updated successfully!!!')


    def getAllHrs(self):
        count=1
        for e in self.employees:
            if e.role.lower()=='hr':
                print(e)
                count+=1
        if count==1:
            raise EmployeeNotExistException('There is no HR as of now!!!')


    def getAllTrainers(self):
        count=1
        for e in self.employees:
            if e.role.lower()=='trainer':
                print(e)
                count+=1
        if count==1:
            raise EmployeeNotExistException('There is no trainer as of now!!!')

    def login(self,id,name):
        for emp in self.employees:
            if emp.id == id and emp.name.lower() == name.lower():
                return emp

        return None

