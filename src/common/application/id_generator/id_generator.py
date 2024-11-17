from abc import ABCMeta, abstractmethod


class IDGenerator(metaclass=ABCMeta):
    @abstractmethod
    def generate(self) -> str:
        pass
