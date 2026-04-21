from engine.models import StockRecord


def score_rebound(record: StockRecord) -> int:
    score = 40
    score += int(abs(record.drawdown_pct) * 3)
    if "rebound" in record.quality_note:
        score += 3
    return max(0, min(score, 100))
