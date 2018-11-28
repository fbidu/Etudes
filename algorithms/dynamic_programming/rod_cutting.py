# -*- encoding: utf-8 -*-
"""
Based on the Rod Cutting problem at [1].


[1]: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest,
and Clifford Stein. 2009. Introduction to Algorithms,
Third Edition(3rd ed.). The MIT Press.
"""

from math import inf
from random import randint
from time import perf_counter


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


def main():
    """
    Main function that benchmarks solutions
    """
    max_size = 22
    sample_pricing = [randint(1, 2000) for _ in range(40)]
    prev_time = 0
    ratio = 0
    for i in range(1, max_size + 1):
        init = perf_counter()
        recursive_cutting(sample_pricing, i)
        final = perf_counter()
        curr_time = final - init

        if prev_time:
            ratio = (curr_time / prev_time) * 100

        prev_time = curr_time
        print("i={0:d} took {1:.4f}s - {2:.1f}% more than the last".format(i, curr_time, ratio))


if __name__ == "__main__":
    main()
