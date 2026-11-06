"""Rank complexity classes by how well they fit a strategy's timings."""

import math
from collections.abc import Sequence
from dataclasses import dataclass
from enum import StrEnum
from typing import cast

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import OptimizeResult, minimize_scalar

type Floats = NDArray[np.float64]

MIN_POINTS = 5  # AICc needs more points than a candidate has parameters + 1
MAX_BASE = 10.0
MAX_EXPONENT = 600.0  # keeps b^n well below float overflow (~e^709)


class Term(StrEnum):
    LOG_N = "log n"
    N = "n"
    N_LOG_N = "n log n"
    N_SQUARED = "n²"
    N_CUBED = "n³"
    EXPONENTIAL = "b^n"  # the base b is fitted

    def evaluate(self, n: Floats, base: float) -> Floats:
        match self:
            case Term.LOG_N:
                return np.log(n)
            case Term.N:
                return n
            case Term.N_LOG_N:
                return n * np.log(n)
            case Term.N_SQUARED:
                return n**2
            case Term.N_CUBED:
                return n**3
            case Term.EXPONENTIAL:
                return base**n


@dataclass(frozen=True)
class Candidate:
    """t ≈ a + c₁·term₁(n) + …: a constant overhead plus one coefficient per term."""

    name: str
    terms: tuple[Term, ...]


CLASSIC: tuple[Candidate, ...] = (
    Candidate("constant", ()),
    *(Candidate(term, (term,)) for term in Term),
)


@dataclass(frozen=True)
class Fit:
    candidate: Candidate
    coefficients: tuple[float, ...]  # a, then one per term
    base: float | None  # fitted b when the candidate has b^n
    aicc: float  # lower is better; only differences between fits matter

    @property
    def name(self) -> str:
        if self.base is None:
            return self.candidate.name
        return self.candidate.name.replace("b^n", f"{self.base:.2f}^n")


@dataclass(frozen=True)
class Growth:
    fits: tuple[Fit, ...]  # best first

    def __str__(self) -> str:
        best, *rest = self.fits
        if not rest:
            return best.name
        gap = rest[0].aicc - best.aicc
        return f"{best.name} (next {rest[0].name} +{gap:.1f})"


def _design(candidate: Candidate, n: Floats, base: float) -> Floats:
    columns = [np.ones_like(n), *(term.evaluate(n, base) for term in candidate.terms)]
    return np.column_stack(columns)


def _solve(design: Floats, seconds: Floats) -> tuple[Floats, float]:
    """Least squares on relative errors, so the slowest size does not
    outweigh all the others. Returns the coefficients and residual sum."""
    weighted = design / seconds[:, np.newaxis]
    target = np.ones_like(seconds)
    coefficients = np.linalg.lstsq(weighted, target)[0]
    return coefficients, float(np.sum((weighted @ coefficients - target) ** 2))


def _fit(candidate: Candidate, n: Floats, seconds: Floats) -> Fit:
    base = None
    if Term.EXPONENTIAL in candidate.terms:
        upper = min(MAX_BASE, math.exp(MAX_EXPONENT / n.max()))
        search = minimize_scalar(
            lambda b: _solve(_design(candidate, n, b), seconds)[1],
            bounds=(1.0, upper),
            method="bounded",
        )
        # scipy's type hints declare the result as a plain object
        base = float(cast(OptimizeResult, search).x)
    coefficients, rss = _solve(_design(candidate, n, base or 0.0), seconds)

    points, params = len(n), len(coefficients) + (base is not None)
    aic = points * math.log(rss / points) + 2 * params
    aicc = aic + 2 * params * (params + 1) / (points - params - 1)
    return Fit(candidate, tuple(float(c) for c in coefficients), base, aicc)


def fit_growth(
    sizes: Sequence[int],
    seconds: Sequence[float],
    extra: Sequence[Candidate] = (),
) -> Growth | None:
    """Fit the CLASSIC candidates plus `extra` to all the points and rank
    them by AICc, best first.

    The constant term absorbs call overhead, so small sizes need not be
    dropped. AICc charges each fitted parameter, so a candidate with more
    terms only wins when it fits clearly better. Returns None with fewer
    than MIN_POINTS points.
    """
    if len(sizes) < MIN_POINTS:
        return None
    n = np.asarray(sizes, dtype=np.float64)
    t = np.asarray(seconds, dtype=np.float64)
    fits = sorted((_fit(c, n, t) for c in (*CLASSIC, *extra)), key=lambda f: f.aicc)
    return Growth(tuple(fits))
