"""Time the strategies of a problem across input sizes."""

import statistics
import timeit
from collections.abc import Callable
from dataclasses import dataclass

from benchmarks.growth import Candidate

DEFAULT_REPEAT = 5


@dataclass(frozen=True)
class Strategy[Input, Output]:
    name: str
    factory: Callable[[], Callable[[Input], Output]]


@dataclass(frozen=True)
class Problem[Input, Output]:
    name: str
    strategies: tuple[Strategy[Input, Output], ...]
    make_input: Callable[[int], Input]
    sizes: tuple[int, ...]  # swept in order, smallest first
    # ranked alongside growth.CLASSIC, for costs specific to this problem
    extra_candidates: tuple[Candidate, ...] = ()


@dataclass(frozen=True)
class Measurement:
    strategy: str
    size: int
    samples: tuple[float, ...]  # seconds per call

    @property
    def median(self) -> float:
        return statistics.median(self.samples)

    @property
    def best(self) -> float:
        return min(self.samples)


type Measure[Input, Output] = Callable[
    [Strategy[Input, Output], int, Input], Measurement
]


def measure[Input, Output](
    strategy: Strategy[Input, Output],
    size: int,
    data: Input,
    repeat: int = DEFAULT_REPEAT,
) -> Measurement:
    """Time one cold call: build a fresh solver and solve, `repeat` times.

    Building the solver inside the timed call costs a little, but it stops
    caches from carrying over between calls.
    """
    timer = timeit.Timer(lambda: strategy.factory()(data))
    number, _ = timer.autorange()
    totals = timer.repeat(repeat=repeat, number=number)
    return Measurement(strategy.name, size, tuple(t / number for t in totals))


def sweep[Input, Output](
    problem: Problem[Input, Output],
    strategy: Strategy[Input, Output],
    budget: float,
    measure: Measure[Input, Output] = measure,
) -> tuple[Measurement, ...]:
    """Measure `strategy` at growing sizes until a call takes over `budget` seconds."""
    measurements: list[Measurement] = []
    for size in problem.sizes:
        measurement = measure(strategy, size, problem.make_input(size))
        measurements.append(measurement)
        if measurement.median > budget:
            break
    return tuple(measurements)
