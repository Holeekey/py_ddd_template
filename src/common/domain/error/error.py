class Error(Exception):
    def __init__(self, message: str, code: str, kind: str, info=None):
        self.message = message
        self.code = code
        self.info = info
        self.kind = kind
        super().__init__(message)
