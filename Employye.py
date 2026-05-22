class employee:
    def __init__(self,name,role,eid):
        self.__eid=eid
        self.__role=role
        self.__name=name
    def getId(self):
        return self.__eid
    def getName(self):
        return self.__name
    def getRole(self):
        return self.__role
    def setRole(self,name):
        self.__name=name
    def setName(self,name):
        self.__name=name   
    def all_details(self):
        print("{} is working as {} in this company".format(self.__name,self.__role))
    
                  