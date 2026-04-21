from pathlib import Path

from engine.pipeline import run_demo_pipeline


def main() -> None:
    report = run_demo_pipeline("data/demo/stocks.json")
    output = Path("reports/examples/demo-report.md")
    output.write_text(report)
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
