from abc import ABCMeta, abstractmethod
from typing import TypeVar

from common.application.result.application_result import AppResult

T = TypeVar("T")
U = TypeVar("R")

class IApplicationService(metaclass=ABCMeta):
    @abstractmethod
    async def execute(self, data: T) -> AppResult[U]:
        pass