"""Time the strategies of a problem across input sizes."""

import statistics
import timeit
from collections.abc import Callable, Mapping
from dataclasses import dataclass

DEFAULT_REPEAT = 5


@dataclass(frozen=True)
class Strategy[I, O]:
    name: str
    factory: Callable[[], Callable[[I], O]]


@dataclass(frozen=True)
class Problem[I, O]:
    name: str
    strategies: tuple[Strategy[I, O], ...]
    make_input: Callable[[int], I]
    sizes: tuple[int, ...]  # swept in order, smallest first
    check_sizes: tuple[int, ...]  # small enough for every strategy to solve


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


class StrategiesDisagree(Exception):
    def __init__(self, size: int, outputs: Mapping[str, object]) -> None:
        self.size = size
        self.outputs = outputs
        answers = ", ".join(f"{name}={output!r}" for name, output in outputs.items())
        super().__init__(f"strategies disagree at size {size}: {answers}")


def check_agreement[I, O](problem: Problem[I, O]) -> None:
    """Raise StrategiesDisagree unless every strategy gives the same output
    at every check size, so a fast but wrong strategy is never timed."""
    for size in problem.check_sizes:
        data = problem.make_input(size)
        outputs = {s.name: s.factory()(data) for s in problem.strategies}
        first, *rest = outputs.values()
        if any(output != first for output in rest):
            raise StrategiesDisagree(size, outputs)


type Measure[I, O] = Callable[[Strategy[I, O], int, I], Measurement]


def measure[I, O](
    strategy: Strategy[I, O], size: int, data: I, repeat: int = DEFAULT_REPEAT
) -> Measurement:
    """Time one cold call: build a fresh solver and solve, `repeat` times.

    Building the solver inside the timed call costs a little, but it stops
    caches from carrying over between calls.
    """
    timer = timeit.Timer(lambda: strategy.factory()(data))
    number, _ = timer.autorange()
    totals = timer.repeat(repeat=repeat, number=number)
    return Measurement(strategy.name, size, tuple(t / number for t in totals))


def sweep[I, O](
    problem: Problem[I, O],
    strategy: Strategy[I, O],
    budget: float,
    measure: Measure[I, O] = measure,
) -> tuple[Measurement, ...]:
    """Measure `strategy` at growing sizes until a call takes over `budget` seconds."""
    measurements: list[Measurement] = []
    for size in problem.sizes:
        measurement = measure(strategy, size, problem.make_input(size))
        measurements.append(measurement)
        if measurement.median > budget:
            break
    return tuple(measurements)
