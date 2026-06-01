from abc import ABC,abstractmethod

class Employee():
    def __init__(self,name, address, salary,  desg ):
        self.name=name
        self.address=address
        self.salary=salary
        self.desg=desg
# bonuses, generating performance reports, and managing projects.
    @abstractmethod
    def bonus(self,amount):
        # self.salary+=amount
        # print('Congratulations, your bonus is',amount)
        pass

    @abstractmethod
    def getPerformance(self):
        # print( 'Your are working good!'
        pass

    @abstractmethod
    def manageProject(self):
        # print( 'You are managing projects in a good way.'
        pass

class Manager(Employee):
    def bonus(self, amount):
        self.salary+=amount
        print('Congratulations, your bonus is',amount)

    def getPerformance(self):
        print( 'Manager is working good!')

    def manageProject(self):
        print( 'Manager is managing projects in a good way.')



class Developer(Employee):
    def bonus(self, amount):
        self.salary+=amount
        print('Congratulations, your bonus is',amount)

    def getPerformance(self):
        print( 'Developer is working good!')

    def manageProject(self):
        print( 'Developer is managing projects in a good way.')


class Programmer(Employee):
    def bonus(self, amount):
        self.salary+=amount
        print('Congratulations, your bonus is',amount)

    def getPerformance(self):
        print( 'Programmer is working good!')

    def manageProject(self):
        print( 'Programmer is managing projects in a good way.')


# e= Employee('employee','USA',12000,'emp')
m= Manager('Alex','USA',5000,'manager')
d= Developer('Smith','UK',45000,'manager')
p= Programmer('John','India',56000,'manager')

m.getPerformance()
d.getPerformance()
p.getPerformance()

m.manageProject()
d.manageProject()
p.manageProject()

m.bonus(1000)
d.bonus(1000)
p.bonus(1000)

