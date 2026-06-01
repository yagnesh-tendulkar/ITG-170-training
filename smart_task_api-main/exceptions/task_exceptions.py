class TaskNotFoundException(Exception):
    def __init__(self,id):
        self.id=id