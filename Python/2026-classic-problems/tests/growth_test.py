import pytest

from benchmarks.growth import Growth, Model, fit_growth


def test_exponential_timings_are_reported_as_exponential():
    """A naive recursive solution doubles its work per step; the report
    must name that as b^n with the right base, not as a steep polynomial."""
    sizes = [10, 15, 20, 25, 30, 35]
    seconds = [1e-6 * 2**n for n in sizes]

    growth = fit_growth(sizes, seconds)

    assert growth is not None
    assert growth.model is Model.EXPONENTIAL
    assert growth.coefficient == pytest.approx(2)


def test_polynomial_timings_are_reported_as_polynomial():
    """A quadratic solution must be named n^2, so two polynomial
    approaches can be told apart by their exponent."""
    sizes = [100, 200, 400, 800, 1600, 3200]
    seconds = [1e-9 * n**2 for n in sizes]

    growth = fit_growth(sizes, seconds)

    assert growth is not None
    assert growth.model is Model.POLYNOMIAL
    assert growth.coefficient == pytest.approx(2)


def test_fit_ignores_overhead_dominated_small_sizes():
    """At small sizes the call overhead hides the algorithm. The fit uses
    only the upper half of the points so that overhead does not skew it."""
    # Setup: flat overhead for the small sizes, n^2 for the large ones
    small = [1, 2, 3, 4]
    large = [10_000, 20_000, 40_000, 80_000]
    sizes = small + large
    seconds = [1e-3] * len(small) + [1e-9 * n**2 for n in large]
    # Sanity check: the small sizes really are flat, which would drag a
    # fit over all points far below n^2
    assert len(set(seconds[: len(small)])) == 1

    # Act
    growth = fit_growth(sizes, seconds)

    # Assert
    assert growth is not None
    assert growth.model is Model.POLYNOMIAL
    assert growth.coefficient == pytest.approx(2)


def test_too_few_points_give_no_estimate():
    """Two points always fit both models perfectly, so any estimate from
    them would be noise presented as a result."""
    assert fit_growth([10, 20], [1e-3, 4e-3]) is None


@pytest.mark.parametrize(
    ("growth", "expected"),
    [
        (Growth(Model.POLYNOMIAL, 1.0234, 0.99912), "n^1.02 (R² 0.999)"),
        (Growth(Model.EXPONENTIAL, 1.6180, 0.99991), "1.62^n (R² 1.000)"),
    ],
)
def test_growth_reads_as_a_complexity(growth, expected):
    """The report prints the estimate next to the timings, so it has to
    read like the complexity notation people already know."""
    assert str(growth) == expected
