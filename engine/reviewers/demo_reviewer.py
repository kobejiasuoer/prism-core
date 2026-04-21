def review_scores(rows: list[tuple[str, int, int]]) -> list[dict[str, int | str]]:
    reviewed = []
    for symbol, momentum, rebound in rows:
        top_score = max(momentum, rebound)
        if top_score >= 70:
            decision = "shortlist"
        elif top_score >= 55:
            decision = "watchlist"
        else:
            decision = "pass"
        reviewed.append(
            {
                "symbol": symbol,
                "momentum": momentum,
                "rebound": rebound,
                "decision": decision,
            }
        )
    return reviewed
