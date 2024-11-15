

class ResponseInfo:
    def __init__(self, code:str, message: str = None):
        self.code = code
        self.message = message

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message
        }