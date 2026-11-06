import pytest

from classic.fibonacci import STRATEGIES, BasicFib

# BasicFib is the recurrence written down as is, so it is the reference.
# It is too slow beyond small n, so large inputs are checked only on the others.
OTHER_STRATEGIES = [cls for cls in STRATEGIES if cls is not BasicFib]


@pytest.mark.parametrize("strategy_class", STRATEGIES, ids=lambda cls: cls.__name__)
def test_fib_calls(strategy_class):
    strategy = strategy_class()
    assert strategy(0) == 0
    assert strategy(1) == 1
    assert strategy(2) == 1
    assert strategy(3) == 2
    assert strategy(8) == 21


@pytest.mark.parametrize("strategy_class", STRATEGIES, ids=lambda cls: cls.__name__)
def test_fibonacci_iter(strategy_class):
    strategy = strategy_class()
    assert list(strategy.iter(5)) == [0, 1, 1, 2, 3]
    assert list(strategy.iter(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


@pytest.mark.parametrize(
    "strategy_class", OTHER_STRATEGIES, ids=lambda cls: cls.__name__
)
def test_strategies_agree_with_the_recurrence(strategy_class):
    """The benchmark only compares speed, so a fast but wrong strategy
    would win it. Each strategy must match the plain recurrence, starting
    cold at every n, as it does in the benchmark."""
    reference = BasicFib()
    for n in range(25):
        assert strategy_class()(n) == reference(n)


@pytest.mark.parametrize(
    "strategy_class", OTHER_STRATEGIES, ids=lambda cls: cls.__name__
)
def test_large_input_matches_known_value(strategy_class):
    """The benchmark runs fast strategies far beyond the sizes the
    reference can reach. A known fib(100) checks them at those sizes."""
    assert strategy_class()(100) == 354_224_848_179_261_915_075
