from engine.adapters.demo_loader import load_demo_stocks


def test_load_demo_stocks_returns_records():
    records = load_demo_stocks("data/demo/stocks.json")

    assert len(records) == 3
    assert records[0].symbol == "DEMO001"
    assert records[0].sector == "AI Infrastructure"
