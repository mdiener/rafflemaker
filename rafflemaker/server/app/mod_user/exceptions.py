class BaseException(Exception):
    def __init__(self, message):
        super().__init__(message)

class UserAlreadyExistsError(BaseException):
    pass

class UserNotFoundError(BaseException):
    pass

class UserResetLinkNotExists(BaseException):
    pass

class CredentialsInvalidError(BaseException):
    pass
