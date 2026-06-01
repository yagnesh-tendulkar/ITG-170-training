class UserAlreadyExistsException(Exception):
    pass


class InvalidCredentialsException(Exception):
    pass


class ResourceNotFoundException(Exception):
    pass


class UnauthorizedAccessException(Exception):
    pass