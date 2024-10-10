from typing import Generic, TypeVar, Optional

from common.domain.utils import is_none, is_not_none

T = TypeVar("T")

class Result(Generic[T]):
    def __init__(
        self, 
        value: Optional[T] = None, 
        error: Optional[Exception] = None
    ) -> None:
        if(is_none(value) and is_none(error)):
            raise ValueError("Value and error cannot be both None")
        if(is_not_none(value) and is_not_none(error)):
            raise ValueError("Value and error cannot be both not None")
        self._value = value
        self._error = error
    
    def is_success(self) -> bool:
        return is_not_none(self._value)
    
    def is_error(self) -> bool:
        return is_not_none(self._error)

    def unwrap(self) -> T:
        if(is_not_none(self._value)):
            return self._value
        raise self._error
    
    def unwrap_or_default(self, default: T) -> T:
        if(is_not_none(self._value)):
            return self._value
        return default
        
    @staticmethod
    def success(value: T) -> "Result[T]":
        return Result(value=value)
    
    @staticmethod
    def failure(error: Exception) -> "Result[T]":
        return Result(error=error)