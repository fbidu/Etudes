"""Estimate how a strategy's running time grows with input size."""

import math
import statistics
from collections.abc import Sequence
from dataclasses import dataclass
from enum import StrEnum

MIN_POINTS = 3


class Model(StrEnum):
    POLYNOMIAL = "polynomial"  # t ≈ c · n^k
    EXPONENTIAL = "exponential"  # t ≈ c · b^n


@dataclass(frozen=True)
class Growth:
    model: Model
    coefficient: float  # k for n^k, b for b^n
    r_squared: float

    def __str__(self) -> str:
        if self.model is Model.POLYNOMIAL:
            shape = f"n^{self.coefficient:.2f}"
        else:
            shape = f"{self.coefficient:.2f}^n"
        return f"{shape} (R² {self.r_squared:.3f})"


@dataclass(frozen=True)
class _Line:
    slope: float
    r_squared: float


def _fit_line(xs: Sequence[float], ys: Sequence[float]) -> _Line:
    slope, _ = statistics.linear_regression(xs, ys)
    return _Line(slope, statistics.correlation(xs, ys) ** 2)


def fit_growth(sizes: Sequence[int], seconds: Sequence[float]) -> Growth | None:
    """Fit n^k and b^n to the upper half of the points and keep the better fit.

    The lower half is dropped because call overhead dominates small sizes.
    Returns None with fewer than MIN_POINTS points.
    """
    if len(sizes) < MIN_POINTS:
        return None
    start = min(len(sizes) // 2, len(sizes) - MIN_POINTS)
    sizes, seconds = sizes[start:], seconds[start:]

    log_seconds = [math.log(s) for s in seconds]
    polynomial = _fit_line([math.log(n) for n in sizes], log_seconds)
    exponential = _fit_line([float(n) for n in sizes], log_seconds)

    if polynomial.r_squared >= exponential.r_squared:
        return Growth(Model.POLYNOMIAL, polynomial.slope, polynomial.r_squared)
    return Growth(Model.EXPONENTIAL, math.exp(exponential.slope), exponential.r_squared)
