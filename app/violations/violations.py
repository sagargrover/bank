

class BaseViolation:
    def __init__(self, code, message):
        self.__code = code
        self.__message = message

    def __str__(self):
        return self.__message

    @property
    def violation_code(self):
        return self.__code


class DuplicateTransactionViolation(BaseViolation):
    def __init__(self):
        code = 409
        message = "doubled-transaction"
        super().__init__(code, message)


class HighFrequencySmallIntervalViolation(BaseViolation):
    def __init__(self):
        code = 429
        message = "high-frequency-small-interval"
        super().__init__(code, message)


class AccountAlreadyIntialized(BaseViolation):
    def __init__(self):
        code = 403
        message = "account-already-initialized"
        super().__init__(code, message)


class InsufficientLimit(BaseViolation):
    def __init__(self):
        code = 401
        message = "insufficient-limit"
        super().__init__(code, message)


class CardNotActive(BaseViolation):
    def __init__(self):
        code = 402
        message = "card-not-active"
        super().__init__(code, message)



