from email.policy import default

import entity
import exceptions
import service
from entity.Employee import Employee
from entity.HR import HR
from entity.Trainee import Trainee
from entity.Trainer import Trainer
from exceptions.OutOfMemoryException import OutOfMemoryException
from service.EmployeeService import EmployeeService


try:
    employeeService = EmployeeService()
    employee= Employee()
    loggedIn = False
    attempts = 3
    try:
        while attempts > 0:
            empId = input('Enter your id : ').lower()
            empName = input('Enter your name : ').lower()
            emp = employeeService.login(int(empId), empName)
            if emp is not None:
                loggedIn = True
                employee = emp
                print(f'Welcome to Employee Management Systems, {emp.name}')
                break
            else:
                loggedIn = False
                attempts -= 1
                print(f'You have entered wrong credentials, chances left: {attempts}')
    except Exception as ex:
        print(ex)
    while (loggedIn ==True):
        print('1.Add Employee\n2.Update Employee\n3.Delete Employee\n4.Fetch all Trainees\n5.Fetch all HRs\n6.Fetch all Trainers\n7.Exit\n')
        choice = int(input('Enter a choice: '))
        match choice:
            case 1:
                id= int(input('Enter employee ID: '))
                name = input('Enter employee name: ')
                role = input('Enter employee role: ')
                age= input('Enter employee age: ')
                salary = float(input('Enter employee salary: '))
                employee=None
                if role.lower() =='hr':
                    employee = HR(id,name, role, age, salary)
                elif role.lower() =='trainer':
                    employee = Trainer(id, name, role, age, salary)
                elif role.lower() =='trainee':
                    employee = Trainee(id, name, role, age, salary)
                else:
                    employee = Employee(id, name, role, age, salary)
                try:
                    if len(employeeService.employees) >20:
                        raise OutOfMemoryException('DB can store max 20 peoples')
                    else:
                        msg = employeeService.addEmployee(employee)
                        print(msg)
                except (OutOfMemoryException,Exception) as e:
                    print("Employee couldn't be added this time, please try again later")

            case 2:
                empId= int(input('Enter employee ID to update: '))
                name= input('Enter new name: ')
                role= input('Enter new role: ')
                age= input('Enter new age: ')
                salary= float(input('Enter new salary: '))
                employee=None
                if role.lower() =='hr':
                    employee = HR(employee, name, role, age, salary)
                elif role.lower() =='trainer':
                    employee = Trainer(employee, name, role, age, salary)
                elif role.lower() =='trainee':
                    employee = Trainee(employee, name, role, age, salary)
                else:
                    employee = Employee(employee, name, role, age, salary)
                try:
                    employeeService.updateEmployee(empId,employee)
                except Exception as e:
                    print(e)

        
            case 3:
                try:
                    empId= int(input('Enter employee ID to delete: '))
                    employeeService.deleteEmployee(empId)
                except Exception as e:
                    print(e)

            case 4:
                try:
                    employeeService.getAllTrainees()
                except Exception as e:
                    print(e)
            case 5:
                try:
                    employeeService.getAllHrs()
                except Exception as e:
                    print(e)
            case 6:
                try:
                    employeeService.getAllTrainers()
                except Exception as e:
                    print(e)

            case 7:
                loggedIn = False
                print('Thank you for your time')
                break
            case _:
                print('Enter a valid choice')
except Exception as e:
    print(e)