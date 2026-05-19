# ================= CUSTOM EXCEPTIONS =================

class InvalidLoginException(Exception):
    pass


class EmployeeNotFoundException(Exception):
    pass


class UnauthorizedAccessException(Exception):
    pass


# ================= BASE CLASS =================

class Employee:

    def __init__(self, name, gmail, password, salary):
        self.name = name
        self.gmail = gmail
        self.password = password
        self.salary = salary

    def display(self):
        print("\n===== Employee Details =====")
        print(f"Name   : {self.name}")
        print(f"Gmail  : {self.gmail}")
        print(f"Salary : {self.salary}")
        print(f"Role   : {self.role}")


# ================= SUBCLASSES =================

class HR(Employee):

    def __init__(self, name, gmail, password, salary):
        super().__init__(name, gmail, password, salary)
        self.role = "HR"


class Trainer(Employee):

    def __init__(self, name, gmail, password, salary):
        super().__init__(name, gmail, password, salary)
        self.role = "Trainer"


class Trainee(Employee):

    def __init__(self, name, gmail, password, salary):
        super().__init__(name, gmail, password, salary)
        self.role = "Trainee"


# ================= EMPLOYEE MANAGEMENT SYSTEM =================

class EmployeeManagementSystem:

    def __init__(self):

        # Dictionary to store employees
        self.employees = {}

        # Default employees
        hr = HR("Bikash HR", "hr@gmail.com", "hr123", 90000)
        trainer = Trainer("Rahul Trainer", "trainer@gmail.com", "trainer123", 60000)
        trainee = Trainee("Ramesh Trainee", "trainee@gmail.com", "trainee123", 25000)

        self.employees[hr.gmail] = hr
        self.employees[trainer.gmail] = trainer
        self.employees[trainee.gmail] = trainee

    # ================= LOGIN =================

    def login(self, gmail, password):

        if gmail in self.employees:

            employee = self.employees[gmail]

            if employee.password == password:
                print("\nLogin Successful")
                print("Logged in as:", employee.role)
                return employee

            else:
                raise InvalidLoginException("Incorrect Password")

        else:
            raise InvalidLoginException("Gmail Not Found")

    # ================= CREATE =================

    def create_employee(self, current_user):

        if current_user.role != "HR":
            raise UnauthorizedAccessException(
                "Only HR can create employees"
            )

        role = input("Enter Role (HR/Trainer/Trainee): ")

        name = input("Enter Name: ")
        gmail = input("Enter Gmail: ")
        password = input("Enter Password: ")
        salary = float(input("Enter Salary: "))

        if role.lower() == "hr":
            employee = HR(name, gmail, password, salary)

        elif role.lower() == "trainer":
            employee = Trainer(name, gmail, password, salary)

        elif role.lower() == "trainee":
            employee = Trainee(name, gmail, password, salary)

        else:
            print("Invalid Role")
            return

        self.employees[gmail] = employee

        print("\nEmployee Created Successfully")

    # ================= READ =================

    def read_employee(self):

        gmail = input("Enter Employee Gmail: ")

        if gmail not in self.employees:
            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        self.employees[gmail].display()

    # ================= UPDATE =================

    def update_employee(self):

        gmail = input("Enter Employee Gmail: ")

        if gmail not in self.employees:
            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        employee = self.employees[gmail]

        print("\n1. Update Name")
        print("2. Update Salary")
        print("3. Update Password")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            employee.name = input("Enter New Name: ")

        elif choice == 2:
            employee.salary = float(input("Enter New Salary: "))

        elif choice == 3:
            employee.password = input("Enter New Password: ")

        else:
            print("Invalid Choice")
            return

        print("\nEmployee Updated Successfully")

    # ================= DELETE =================

    def delete_employee(self, current_user):

        if current_user.role not in ["HR", "Trainer"]:
            raise UnauthorizedAccessException(
                "You are not allowed to delete employees"
            )

        gmail = input("Enter Employee Gmail to Delete: ")

        if gmail not in self.employees:
            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        del self.employees[gmail]

        print("\nEmployee Deleted Successfully")

    # ================= READ ALL =================

    def read_all(self, current_user):

        if current_user.role != "HR":
            raise UnauthorizedAccessException(
                "Only HR can view all employees"
            )

        print("\n======= ALL EMPLOYEES =======")

        for employee in self.employees.values():
            employee.display()


# ================= MAIN PROGRAM =================

ems = EmployeeManagementSystem()

try:

    gmail = input("Enter Gmail: ")
    password = input("Enter Password: ")

    current_user = ems.login(gmail, password)

    while True:

        print("\n========= MENU =========")

        # HR MENU
        if current_user.role == "HR":

            print("1. Create Employee")
            print("2. Read Employee")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Read All Employees")
            print("6. Exit")

        # TRAINER MENU
        elif current_user.role == "Trainer":

            print("1. Read Employee")
            print("2. Update Employee")
            print("3. Delete Employee")
            print("4. Exit")

        # TRAINEE MENU
        elif current_user.role == "Trainee":

            print("1. Read Employee")
            print("2. Update Employee")
            print("3. Exit")

        choice = int(input("Enter Your Choice: "))

        # ================= HR OPERATIONS =================

        if current_user.role == "HR":

            if choice == 1:
                ems.create_employee(current_user)

            elif choice == 2:
                ems.read_employee()

            elif choice == 3:
                ems.update_employee()

            elif choice == 4:
                ems.delete_employee(current_user)

            elif choice == 5:
                ems.read_all(current_user)

            elif choice == 6:
                print("Exiting Program")
                break

            else:
                print("Invalid Choice")

        # ================= TRAINER OPERATIONS =================

        elif current_user.role == "Trainer":

            if choice == 1:
                ems.read_employee()

            elif choice == 2:
                ems.update_employee()

            elif choice == 3:
                ems.delete_employee(current_user)

            elif choice == 4:
                print("Exiting Program")
                break

            else:
                print("Invalid Choice")

        # ================= TRAINEE OPERATIONS =================

        elif current_user.role == "Trainee":

            if choice == 1:
                ems.read_employee()

            elif choice == 2:
                ems.update_employee()

            elif choice == 3:
                print("Exiting Program")
                break

            else:
                print("Invalid Choice")

except InvalidLoginException as e:
    print("\nLogin Error:", e)

except EmployeeNotFoundException as e:
    print("\nEmployee Error:", e)

except UnauthorizedAccessException as e:
    print("\nAccess Error:", e)

except Exception as e:
    print("\nUnexpected Error:", e)