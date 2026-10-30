from app.pricing.price_analyzer import analyze_prices


def test_analyze_prices():
    result = analyze_prices([100.0, 100.0, 100.0])

    assert result["lowest_price"] == 100.0
    assert result["highest_price"] == 100.0
    assert result["average_price"] == 100.0
    assert result["competitors_count"] == 3