from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    min_price_seen = float('inf')
    max_profit = 0.0
    for price in prices:
        # know that we need to iterate over the whole thing, idx doesn't matter
        min_price_seen = min(min_price_seen, price)
        max_profit = max(max_profit, price - min_price_seen)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
