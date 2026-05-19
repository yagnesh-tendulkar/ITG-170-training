# ================= CUSTOM EXCEPTIONS =================

class AccessDeniedException(Exception):
    pass


class EmployeeNotFoundException(Exception):
    pass


class InvalidLoginException(Exception):
    pass


# ================= BASE CLASS =================

class Employee:

    employees = {}

    users = {

        "hr@gmail.com": {
            "password": "hr123",
            "role": "HR"
        },

        "trainer@gmail.com": {
            "password": "trainer123",
            "role": "Trainer"
        },

        "trainee@gmail.com": {
            "password": "trainee123",
            "role": "Trainee"
        }
    }

    def __init__(self, emp_id, name, salary):

        self.emp_id = emp_id
        self.name = name
        self.salary = salary


# ================= HR CLASS =================

class HR(Employee):

    # CREATE

    def create_employee(self, emp_id, name, salary):

        Employee.employees[emp_id] = {

            "Name": name,
            "Salary": salary
        }

        print("Employee Added Successfully")

    # READ SINGLE

    def read_employee(self, emp_id):

        if emp_id not in Employee.employees:

            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        print(Employee.employees[emp_id])

    # READ ALL

    def read_all_employees(self):

        if len(Employee.employees) == 0:

            print("No Employees Found")

        else:

            print("\n====== EMPLOYEE DATA ======")

            for emp_id, details in Employee.employees.items():

                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Salary:", details["Salary"])
                print("---------------------------")

    # UPDATE

    def update_employee(self, emp_id, name, salary):

        if emp_id not in Employee.employees:

            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        Employee.employees[emp_id] = {

            "Name": name,
            "Salary": salary
        }

        print("Employee Updated Successfully")

    # DELETE

    def delete_employee(self, emp_id):

        if emp_id not in Employee.employees:

            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        del Employee.employees[emp_id]

        print("Employee Deleted Successfully")


# ================= TRAINER CLASS =================

class Trainer(Employee):

    # READ SINGLE

    def read_employee(self, emp_id):

        if emp_id not in Employee.employees:

            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        print(Employee.employees[emp_id])

    # READ ALL

    def read_all_employees(self):

        if len(Employee.employees) == 0:

            print("No Employees Found")

        else:

            print("\n====== EMPLOYEE DATA ======")

            for emp_id, details in Employee.employees.items():

                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Salary:", details["Salary"])
                print("---------------------------")

    # UPDATE

    def update_employee(self, emp_id, name, salary):

        if emp_id not in Employee.employees:

            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        Employee.employees[emp_id] = {

            "Name": name,
            "Salary": salary
        }

        print("Employee Updated Successfully")

    # DELETE

    def delete_employee(self, emp_id):

        if emp_id not in Employee.employees:

            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        del Employee.employees[emp_id]

        print("Employee Deleted Successfully")


# ================= TRAINEE CLASS =================

class Trainee(Employee):

    # READ SINGLE

    def read_employee(self, emp_id):

        if emp_id not in Employee.employees:

            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        print(Employee.employees[emp_id])

    # READ ALL

    def read_all_employees(self):

        if len(Employee.employees) == 0:

            print("No Employees Found")

        else:

            print("\n====== EMPLOYEE DATA ======")

            for emp_id, details in Employee.employees.items():

                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Salary:", details["Salary"])
                print("---------------------------")

    # UPDATE

    def update_employee(self, emp_id, name, salary):

        if emp_id not in Employee.employees:

            raise EmployeeNotFoundException(
                "Employee Not Found"
            )

        Employee.employees[emp_id] = {

            "Name": name,
            "Salary": salary
        }

        print("Employee Updated Successfully")


# ================= OBJECTS =================

hr = HR(1, "HR", 90000)

trainer = Trainer(2, "Trainer", 60000)

trainee = Trainee(3, "Trainee", 30000)


# ================= INITIAL DATA =================

Employee.employees[101] = {

    "Name": "Bikash",
    "Salary": 50000
}

Employee.employees[102] = {

    "Name": "Rahul",
    "Salary": 45000
}

Employee.employees[103] = {

    "Name": "Aman",
    "Salary": 40000
}


# ================= LOGIN SYSTEM =================

try:

    gmail = input("Enter Gmail: ")

    password = input("Enter Password: ")

    # VERIFY GMAIL

    if gmail not in Employee.users:

        raise InvalidLoginException(
            "Invalid Gmail"
        )

    # VERIFY PASSWORD

    if Employee.users[gmail]["password"] != password:

        raise InvalidLoginException(
            "Invalid Password"
        )

    # FETCH ROLE

    role = Employee.users[gmail]["role"]

    print("\nLogin Successful")
    print("Logged in as:", role)

    # ROLE MAPPING

    if role == "HR":

        user = hr

    elif role == "Trainer":

        user = trainer

    else:

        user = trainee


    # ================= MENU =================

    while True:

        print("\n========== MENU ==========")

        # ===== HR MENU =====

        if role == "HR":

            print("1. Create Employee")
            print("2. Read Employee")
            print("3. Read All Employees")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")

            choice = int(input("Enter Choice: "))

            # CREATE

            if choice == 1:

                emp_id = int(input("Enter Employee ID: "))
                name = input("Enter Name: ")
                salary = float(input("Enter Salary: "))

                user.create_employee(
                    emp_id,
                    name,
                    salary
                )

            # READ SINGLE

            elif choice == 2:

                emp_id = int(input(
                    "Enter Employee ID: "
                ))

                user.read_employee(emp_id)

            # READ ALL

            elif choice == 3:

                user.read_all_employees()

            # UPDATE

            elif choice == 4:

                emp_id = int(input(
                    "Enter Employee ID: "
                ))

                name = input("Enter New Name: ")

                salary = float(input(
                    "Enter New Salary: "
                ))

                user.update_employee(
                    emp_id,
                    name,
                    salary
                )

            # DELETE

            elif choice == 5:

                emp_id = int(input(
                    "Enter Employee ID: "
                ))

                user.delete_employee(emp_id)

            # EXIT

            elif choice == 6:

                print("Exiting Program...")
                break

            else:

                print("Invalid Choice")


        # ===== TRAINER MENU =====

        elif role == "Trainer":

            print("1. Read Employee")
            print("2. Read All Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Exit")

            choice = int(input("Enter Choice: "))

            # READ SINGLE

            if choice == 1:

                emp_id = int(input(
                    "Enter Employee ID: "
                ))

                user.read_employee(emp_id)

            # READ ALL

            elif choice == 2:

                user.read_all_employees()

            # UPDATE

            elif choice == 3:

                emp_id = int(input(
                    "Enter Employee ID: "
                ))

                name = input("Enter New Name: ")

                salary = float(input(
                    "Enter New Salary: "
                ))

                user.update_employee(
                    emp_id,
                    name,
                    salary
                )

            # DELETE

            elif choice == 4:

                emp_id = int(input(
                    "Enter Employee ID: "
                ))

                user.delete_employee(emp_id)

            # EXIT

            elif choice == 5:

                print("Exiting Program...")
                break

            else:

                print("Invalid Choice")


        # ===== TRAINEE MENU =====

        else:

            print("1. Read Employee")
            print("2. Read All Employees")
            print("3. Update Employee")
            print("4. Exit")

            choice = int(input("Enter Choice: "))

            # READ SINGLE

            if choice == 1:

                emp_id = int(input(
                    "Enter Employee ID: "
                ))

                user.read_employee(emp_id)

            # READ ALL

            elif choice == 2:

                user.read_all_employees()

            # UPDATE

            elif choice == 3:

                emp_id = int(input(
                    "Enter Employee ID: "
                ))

                name = input("Enter New Name: ")

                salary = float(input(
                    "Enter New Salary: "
                ))

                user.update_employee(
                    emp_id,
                    name,
                    salary
                )

            # EXIT

            elif choice == 4:

                print("Exiting Program...")
                break

            else:

                print("Invalid Choice")


except InvalidLoginException as e:

    print("Exception:", e)


except EmployeeNotFoundException as e:

    print("Exception:", e)


except Exception as e:

    print("Exception:", e)