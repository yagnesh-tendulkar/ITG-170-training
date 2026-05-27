class validationException(Exception):
    def __init__(self,message,code):
        self.message=message
        self.code=code
        super().__init__(message)

try:
    print("this is the code for the Custom Exception using Exception")
    raise validationException("invalid message",101)
except validationException as e:
    print(e)