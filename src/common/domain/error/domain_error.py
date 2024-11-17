from .error import Error

class DomainError(Error):
    def __init__(self, message: str, code: str, info=None):
        super().__init__(
            message = message,
            code = code, kind = 'DOMAIN',
            info = info
        )