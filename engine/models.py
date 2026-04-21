from dataclasses import dataclass


@dataclass(slots=True)
class StockRecord:
    symbol: str
    name: str
    sector: str
    price_change_pct: float
    volume_change_pct: float
    drawdown_pct: float
    quality_note: str
