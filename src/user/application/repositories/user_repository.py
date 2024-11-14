from abc import ABCMeta, abstractmethod
from typing import List, Optional

from common.domain.result.result import Result
from user.application.models.user import User


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_one(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def find_all(self) -> Optional[List[User]]:
        pass

    @abstractmethod
    def save(self, user: User) -> Result[User]:
        pass