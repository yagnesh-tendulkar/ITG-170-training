#classmethod
class Robot:
    process=0#classattribute
    @classmethod
    def add(cls):
        """Class method :method that changes all the istances of class
         here w created a class method  to increment the process count"""
        cls.process+=1
        print("Process:",cls.process)
class Android(Robot):
    """In this example, we have a Robot class with a class attribute process and a class method add() that increments 
    the process count. The Android class inherits from Robot and can call the add() method to increment
      the process count for all instances of the Robot class."""
    pass
a1=Android()
a2=Android()
a1.add()#calling class method using instance
a2.add()#calling class method using instance
#Robot.add()
#Robot.add() 