# -*- encoding: utf-8 -*-
"""
Based on the Rod Cutting problem at [1].


[1]: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest,
and Clifford Stein. 2009. Introduction to Algorithms,
Third Edition(3rd ed.). The MIT Press.
"""

from functools import lru_cache
from math import inf
from random import randint
from time import perf_counter

from benchmark import benchmark


def recursive_cutting(price_table, size):
    """
    Given a price table p and size n, find the maximum
    revenue possible
    """
    if size == 0:
        return 0

    max_revenue = -inf
    for i in range(1, size + 1):
        max_revenue = max(
            max_revenue, price_table[i - 1] + recursive_cutting(price_table, size - i)
        )
    return max_revenue

@lru_cache(maxsize=None)
def recursive_cutting_lru_cached(price_table, size):
    """
    Given a price table p and size n, find the maximum
    revenue possible
    """
    if size == 0:
        return 0

    max_revenue = -inf
    for i in range(1, size + 1):
        max_revenue = max(
            max_revenue, price_table[i - 1] + recursive_cutting(price_table, size - i)
        )
    return max_revenue

def rod_cutting_memoized_top_down(price_table, size):
    """
    This function caches the price for bigger rods.
    It uses a top-down memoization
    """
    cache = [-inf for _ in range(size)]

    def rod_cut(price_table, size, cache):
        if cache[size - 1] >= 0:
            return cache[size - 1]

        if not size:
            max_revenue = 0
        else:
            max_revenue = -inf
            for i in range(1, size):
                max_revenue = max(
                    max_revenue, price_table[i - 1] + rod_cut(price_table, size - i, cache)
                )
        cache[size - 1] = max_revenue
        return max_revenue

    return rod_cut(price_table, size, cache)

def rod_cutting_memoized_bottom_up(price_table, size):
    cache = [0 for _ in range(size)]
    for j in range(size):
        max_revenue = -inf
        for i in range(0, j + 1):
            max_revenue = max(
                max_revenue, price_table[i] + cache[j - i - 1]
            )
        cache[j] = max_revenue
    return cache[size - 1]

def main():
    """
    Main function that benchmarks solutions
    """
    max_size = 22
    sample_pricing = [randint(1, 2000) for _ in range(40)]

    print("Benchmarking recursive cutting with list of prices:")
    benchmark(recursive_cutting, [sample_pricing], range(1, max_size + 1))

    """
    Simple LRU caching does not help this problem. I have commented this out to
    speed up the benchmarkings. Bottom up memoization is way faster
    
    print("Benchmarking recursive cutting with list of prices LRU Cached:")
    sample_pricing = tuple(randint(1, 2000) for _ in range(40))
    benchmark(recursive_cutting_lru_cached, [sample_pricing], range(1, max_size + 1))
    """
    
    print("Benchmarking recursive cutting with top-down memoization:")
    sample_pricing = tuple(randint(1, 2000) for _ in range(40))
    benchmark(rod_cutting_memoized_top_down, [sample_pricing], range(1, max_size + 1))

    print("Benchmarking recursive cutting with bottom-up memoization:")
    sample_pricing = tuple(randint(1, 2000) for _ in range(40))
    benchmark(rod_cutting_memoized_bottom_up, [sample_pricing], range(1, max_size + 1))
if __name__ == "__main__":
    main()
