import math

from benchmarks.growth import Candidate, Fit, Growth, Term, fit_growth

SIZES = [40, 100, 200, 400, 800, 1600]


def _noisy(seconds: list[float]) -> list[float]:
    """Real timings never sit exactly on a curve; ±1% keeps the tests honest."""
    return [s * (1.01 if i % 2 else 0.99) for i, s in enumerate(seconds)]


def _best(sizes: list[int], seconds: list[float], *extra: Candidate) -> str:
    growth = fit_growth(sizes, seconds, extra)
    assert growth is not None
    return growth.fits[0].name


def test_linear_timings_beat_n_log_n():
    """n and n log n look alike on a log-log plot. Ranking named shapes
    must still tell a linear strategy apart from an n log n one."""
    seconds = _noisy([2e-7 + 1.4e-7 * n for n in SIZES])

    assert _best(SIZES, seconds) == "n"


def test_n_log_n_timings_beat_linear():
    """The reverse case: a sort-like strategy must not be called linear."""
    seconds = _noisy([2e-7 + 2e-8 * n * math.log(n) for n in SIZES])

    assert _best(SIZES, seconds) == "n log n"


def test_exponential_timings_report_their_base():
    """For naive recursion the base is the interesting number (φ for
    Fibonacci), so it is fitted and shown, not just "exponential"."""
    sizes = [5, 10, 15, 20, 25, 30, 35]
    seconds = _noisy([1e-7 + 1e-9 * 2**n for n in sizes])

    assert _best(sizes, seconds) == "2.00^n"


def test_overhead_does_not_hide_the_shape():
    """At small sizes the call overhead dominates. The constant term
    absorbs it, so every point can be used without skewing the shape."""
    # Setup: a flat millisecond of overhead until n² takes over
    sizes = [10, 100, 1_000, 3_000, 10_000, 30_000, 100_000]
    seconds = _noisy([1e-3 + 1e-9 * n**2 for n in sizes])
    # Sanity check: the two smallest sizes are flat, i.e. all overhead
    assert max(seconds[:2]) / min(seconds[:2]) < 1.05

    # Act / Assert
    assert _best(sizes, seconds) == "n²"


def test_problem_specific_candidates_join_the_ranking():
    """Some problems have a known extra cost, like big-int additions in
    Fibonacci. A candidate for it must be able to win the ranking."""
    # Setup: linear work plus a growing n² part, as in memoized Fibonacci
    seconds = _noisy([2e-7 + 1.3e-7 * n + 3e-11 * n**2 for n in SIZES])
    mixed = Candidate("n + n²", (Term.N, Term.N_SQUARED))
    # Sanity check: without the extra candidate, a classic shape wins
    assert _best(SIZES, seconds) != "n + n²"

    # Act / Assert
    assert _best(SIZES, seconds, mixed) == "n + n²"


def test_too_few_points_give_no_ranking():
    """With barely more points than parameters every candidate fits, so a
    ranking would be noise presented as a result."""
    assert fit_growth([10, 20, 30, 40], [1e-3, 2e-3, 3e-3, 4e-3]) is None


def test_growth_names_the_best_fit_and_its_lead():
    """The table shows one line per strategy: the winner, and how far
    ahead of the runner-up it is, since a small gap means a tie."""
    linear = Fit(Candidate("n", (Term.N,)), (1e-7, 1e-9), None, -90.0)
    n_log_n = Fit(Candidate("n log n", (Term.N_LOG_N,)), (1e-7, 1e-10), None, -68.8)

    assert str(Growth((linear, n_log_n))) == "n (next n log n +21.2)"


def test_exponential_fit_is_named_by_its_fitted_base():
    """A bare "b^n" would hide the base, which is the result people want."""
    exponential = Fit(Candidate("b^n", (Term.EXPONENTIAL,)), (0, 1e-7), 1.618, -50)

    assert exponential.name == "1.62^n"
