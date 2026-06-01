class TaskNotFoundException(Exception):
    """
    Raised when a task is not found.
    """

    def __init__(
        self,
        message: str = "Task not found"
    ):
        self.message = message
        super().__init__(self.message)


class UserNotFoundException(Exception):
    """
    Raised when a user is not found.
    """

    def __init__(
        self,
        message: str = "User not found"
    ):
        self.message = message
        super().__init__(self.message)


class FileValidationException(Exception):
    """
    Raised when uploaded file validation fails.
    """

    def __init__(
        self,
        message: str = "Invalid file"
    ):
        self.message = message
        super().__init__(self.message)


class AuthenticationException(Exception):
    """
    Raised when authentication fails.
    """

    def __init__(
        self,
        message: str = "Authentication failed"
    ):
        self.message = message
        super().__init__(self.message)


class AuthorizationException(Exception):
    """
    Raised when user is not authorized.
    """

    def __init__(
        self,
        message: str = "Access denied"
    ):
        self.message = message
        super().__init__(self.message)