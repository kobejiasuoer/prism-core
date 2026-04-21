from engine.adapters.demo_loader import load_demo_stocks
from engine.reports.markdown_report import build_markdown_report
from engine.reviewers.demo_reviewer import review_scores
from engine.scorers.momentum_demo import score_momentum
from engine.scorers.rebound_demo import score_rebound


def run_demo_pipeline(path: str) -> str:
    records = load_demo_stocks(path)
    scored = [(record.symbol, score_momentum(record), score_rebound(record)) for record in records]
    reviewed = review_scores(scored)
    return build_markdown_report(reviewed)
