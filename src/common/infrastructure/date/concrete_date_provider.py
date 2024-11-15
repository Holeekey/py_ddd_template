import datetime

from common.application.date.date_provider import DateProvider


class ConcreteDateProvider(DateProvider):
    def get_date(self) -> datetime:
        return datetime.now()