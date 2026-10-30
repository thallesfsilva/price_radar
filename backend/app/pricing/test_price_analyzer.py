from price_analyzer import analyze_prices
from decimal import Decimal

prices = [
    Decimal("3499.90"),
    Decimal("3299.90"),
    Decimal("3599.90"),
    Decimal("3099.90"),
    Decimal("3399.90")
]

result = analyze_prices(prices)

print(result)