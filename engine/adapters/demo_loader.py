import json
from pathlib import Path

from engine.models import StockRecord


def load_demo_stocks(path: str) -> list[StockRecord]:
    raw = json.loads(Path(path).read_text())
    return [StockRecord(**item) for item in raw]
