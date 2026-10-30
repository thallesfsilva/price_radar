from decimal import Decimal

def analyze_prices(prices: list[Decimal]) -> dict[str, Decimal | int | None]:
    if not prices:
        return {
            "lowest_price": None,
            "highest_price": None,
            "average_price": None,
            "competitors_count": 0
        }

    lowest_price = min(prices)
    highest_price = max(prices)
    soma = Decimal("0")
    for i in prices:
        soma += i
    competitors_count = len(prices)
    average_prices = soma/competitors_count

    retorno = {
        "lowest_price": lowest_price,
        "highest_price": highest_price,
        "average_price": average_prices,
        "competitors_count": competitors_count
    }
    
    return retorno
    