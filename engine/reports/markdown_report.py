def build_markdown_report(rows: list[dict[str, int | str]]) -> str:
    lines = [
        "# Prism Demo Report",
        "",
        "| Symbol | Momentum | Rebound | Decision |",
        "| --- | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['symbol']} | {row['momentum']} | {row['rebound']} | {row['decision']} |"
        )
    return "\n".join(lines) + "\n"
