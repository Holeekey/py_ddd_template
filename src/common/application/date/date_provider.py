from abc import ABCMeta, abstractmethod
import datetime


class DateProvider(metaclass=ABCMeta):
    @abstractmethod
    def current(self) -> datetime:
        pass
