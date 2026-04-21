from engine.models import StockRecord


def score_momentum(record: StockRecord) -> int:
    score = 50
    score += int(record.price_change_pct * 3)
    score += int(record.volume_change_pct / 2)
    return max(0, min(score, 100))
