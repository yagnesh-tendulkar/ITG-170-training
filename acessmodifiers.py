class Demo:
    name="static varible"
    def __init__(self,a,b,c):
        self.public=a
        self._protected=b
        self.__private=c
    def publicMethod(self):
        print("it is a public method{}".format(self.public))  
    def _prometh(self):
        print("it is a protected method") 
    def __p_meth(self):
        print("private method")
    @staticmethod
    def s_meth():
        print("this is static method and {}".format(Demo.name))
ob=Demo(1,2,3)
ob.publicMethod()
ob._prometh()
ob.s_meth()
#ob.__p_meth()// it is private method we can not acess it outwide the class
        
                     
        