from datetime import datetime

class DomainEvent:
    def __init__(self, name: str):
        self._event_time = datetime.now()
        self._name = name

    @property
    def event_time(self) -> datetime:
        return self._event_time

    @property
    def name(self) -> str:
        return self._name   