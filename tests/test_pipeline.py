from engine.pipeline import run_demo_pipeline


def test_run_demo_pipeline_returns_markdown_report():
    report = run_demo_pipeline("data/demo/stocks.json")

    assert "# Prism Demo Report" in report
    assert "DEMO001" in report
    assert "shortlist" in report
