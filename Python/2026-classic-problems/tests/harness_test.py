from benchmarks.harness import Measurement, Problem, Strategy, measure, sweep


def _identity_problem(sizes: tuple[int, ...]) -> Problem[int, int]:
    return Problem(
        name="identity",
        strategies=(Strategy("identity", lambda: lambda n: n),),
        make_input=lambda n: n,
        sizes=sizes,
        check_sizes=(),
    )


def test_measure_builds_a_fresh_solver_for_every_call():
    """A solver that caches between calls, like a memoized one, would be
    timed on cache hits. One solver per call keeps every timed call cold."""
    # Setup
    built = 0
    calls = 0

    def factory():
        nonlocal built
        built += 1

        def solve(n: int) -> int:
            nonlocal calls
            calls += 1
            return n

        return solve

    # Act
    measurement = measure(Strategy("counting", factory), size=1, data=1, repeat=3)

    # Assert
    assert calls > 0
    assert built == calls
    assert len(measurement.samples) == 3


def test_sweep_stops_after_the_first_size_over_budget():
    """Exponential strategies blow up within a few sizes. Stopping right
    after the first size over budget caps the cost at one slow point."""
    problem = _identity_problem(sizes=(1, 2, 3, 4, 5))
    seconds = {1: 0.01, 2: 0.1, 3: 1.0, 4: 10.0, 5: 100.0}

    def fake_measure(strategy: Strategy[int, int], size: int, data: int) -> Measurement:
        return Measurement(strategy.name, size, (seconds[size],))

    measurements = sweep(
        problem, problem.strategies[0], budget=0.5, measure=fake_measure
    )

    assert [m.size for m in measurements] == [1, 2, 3]


def test_sweep_builds_each_input_from_its_size():
    """Problems whose input is not the size itself, like a list to sort,
    rely on make_input to turn each size into real data."""
    problem = Problem(
        name="sum",
        strategies=(Strategy("sum", lambda: sum),),
        make_input=lambda n: list(range(n)),
        sizes=(2, 3),
        check_sizes=(),
    )
    seen: list[list[int]] = []

    def fake_measure(
        strategy: Strategy[list[int], int], size: int, data: list[int]
    ) -> Measurement:
        seen.append(data)
        return Measurement(strategy.name, size, (0.0,))

    sweep(problem, problem.strategies[0], budget=1.0, measure=fake_measure)

    assert seen == [[0, 1], [0, 1, 2]]
