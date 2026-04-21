from typing import Protocol

from engine.models import StockRecord


class Scorer(Protocol):
    def __call__(self, record: StockRecord) -> int:
        ...
