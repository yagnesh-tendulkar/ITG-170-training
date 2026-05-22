#Program to Show Usage of Static keyword in Class
class College:

    college_name = "GVP"


    def show(self):

        print(College.college_name)


obj1 = College()
obj2 = College()

obj1.show()
obj2.show()