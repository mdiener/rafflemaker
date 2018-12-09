class BaseException(Exception):
    def __init__(self, message):
        super().__init__(message)


class RaffleError(BaseException):
    pass


class RaffleCreationError(RaffleError):
    pass


class RaffleParameterError(RaffleError):
    pass


class RaffleNotFoundError(RaffleError):
    pass


class RaffleAlreadyExistsError(RaffleError):
    pass


class ContestantError(BaseException):
    pass


class ContestantNotFoundError(ContestantError):
    pass


class ContestantAlreadyExistsError(ContestantError):
    pass


class ContestantParameterError(ContestantError):
    pass
