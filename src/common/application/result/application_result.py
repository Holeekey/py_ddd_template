from typing import Generic, Optional, TypeVar
from common.domain.result.result import Result

T = TypeVar("T")

class ResultInfo:
    def __init__(self, code: str, message: str):
        self._code = code
        self._message = message

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message

class AppResult(Result,Generic[T]):
    def __init__(
        self, 
        value: Optional[T] = None, 
        error: Optional[Exception] = None,
        info: Optional[ResultInfo] = None
    ):
        super().__init__(value, error)
        self._info = info

    @staticmethod
    def success(value,info: ResultInfo):
        return AppResult(value=value, info=info)

    @staticmethod
    def failure(error):
        return AppResult(error=error)