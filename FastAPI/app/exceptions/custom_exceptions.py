class UserNotFoundException(Exception):

    def __init__(self):

        self.message = "User not found"


class UserAlreadyExistsException(Exception):

    def __init__(self):

        self.message = "User already exists"