from typing import Callable, Generic, Optional, TypeVar
from common.application.error.application_error import ApplicationError
from common.domain.result.result import Result
from common.domain.utils.is_none import is_none
from common.domain.utils.is_not_none import is_not_none

T = TypeVar("T")
R = TypeVar("R")

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
    
    def to_dict(self):
        return {
            "code": self._code,
            "message": self._message
        }

class AppResult(Result,Generic[T]):
    def __init__(
        self, 
        value: Optional[T] = None, 
        error: Optional[ApplicationError] = None,
        info: Optional[ResultInfo] = None
    ):
        super().__init__(value, error)
        self._info = info

    def handleSuccess(self,handler: Callable[[T, ResultInfo], R]):
        if(is_none(self._value)):
            raise Exception("Cannot handle without value")    
        return handler(self._value, self._info)

    def unwrap(self) -> T:
        if(is_not_none(self._value)):
            return {
                "info": self._info.to_dict(),
                "result": self._value
            }
        raise self._error

    @staticmethod
    def success(value: T,info: ResultInfo):
        return AppResult(value=value, info=info)

    @staticmethod
    def failure(error: ApplicationError):
        return AppResult(error=error)