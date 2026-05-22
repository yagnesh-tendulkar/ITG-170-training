class Employee:

  
    def __init__(self, name, department, salary):

        # Public 
        self.name = name

        # Protected 
        self._department = department

        # Private 
        self.__salary = salary


    def display_public(self):
        print("Public Data")
        print("Employee Name:", self.name)


    def _display_protected(self):
        print("\nProtected Data")
        print("Department:", self._department)

    
    def __display_private(self):
        print("\nPrivate Data")
        print("Salary:", self.__salary)

    # Method to access private method
    def access_private(self):
        self.__display_private()



emp = Employee("Arika", "Python Development", 50000)


emp.display_public()


emp._display_protected()


emp.access_private()



