import pytest

from classic.fibonacci import basic_fib, memoized_fib

strategies = [basic_fib, memoized_fib]


@pytest.mark.parametrize("strategy", strategies)
def test_fib_calls(strategy):
    assert strategy(0) == 0
    assert strategy(1) == 1
    assert strategy(2) == 1
    assert strategy(3) == 2
    assert strategy(8) == 21


@pytest.mark.parametrize("strategy", strategies)
def test_fibonacci_iter(strategy):
    assert list(strategy.iter(5)) == [0, 1, 1, 2, 3]
    assert list(strategy.iter(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
