from engine.models import StockRecord
from engine.reviewers.demo_reviewer import review_scores
from engine.scorers.momentum_demo import score_momentum
from engine.scorers.rebound_demo import score_rebound


def test_momentum_demo_prefers_positive_price_and_volume():
    record = StockRecord(
        "DEMO001",
        "Atlas Compute",
        "AI Infrastructure",
        4.8,
        21.0,
        -3.2,
        "steady growth",
    )
    assert score_momentum(record) == 74


def test_rebound_demo_prefers_deeper_drawdown_with_stable_note():
    record = StockRecord(
        "DEMO002",
        "Harbor Motors",
        "EV Components",
        -2.4,
        -10.0,
        -8.5,
        "rebound candidate",
    )
    assert score_rebound(record) == 68


def test_review_scores_returns_shortlist_and_watchlist():
    reviewed = review_scores(
        [
            ("DEMO001", 74, 40),
            ("DEMO002", 35, 68),
            ("DEMO003", 52, 44),
        ]
    )

    assert reviewed[0]["decision"] == "shortlist"
    assert reviewed[1]["decision"] == "watchlist"
