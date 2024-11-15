class ApplicationError(Exception):
    def __init__(self, message: str, code: str, info=None):
        self.message = message
        self.code = code
        self.info = info
        self.kind = 'application'
        super().__init__(message)