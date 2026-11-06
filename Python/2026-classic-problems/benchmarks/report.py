"""Show sweep results as a table and save them as JSON."""

import json
import platform
import subprocess
import sys
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

from benchmarks.growth import Candidate, Growth, fit_growth
from benchmarks.harness import Measurement

_UNITS = ((1e-6, 1e9, "ns"), (1e-3, 1e6, "µs"), (1.0, 1e3, "ms"))


@dataclass(frozen=True)
class StrategyResult:
    strategy: str
    measurements: tuple[Measurement, ...]
    growth: Growth | None

    @classmethod
    def from_sweep(
        cls,
        strategy: str,
        measurements: tuple[Measurement, ...],
        extra_candidates: tuple[Candidate, ...] = (),
    ) -> StrategyResult:
        growth = fit_growth(
            [m.size for m in measurements],
            [m.median for m in measurements],
            extra_candidates,
        )
        return cls(strategy, measurements, growth)


def _git(*args: str) -> str | None:
    try:
        completed = subprocess.run(
            ["git", *args], capture_output=True, text=True, check=True
        )
    except OSError, subprocess.CalledProcessError:
        return None
    return completed.stdout.strip()


@dataclass(frozen=True)
class Metadata:
    python: str
    platform: str
    jit_enabled: bool | None  # None when this build has no JIT
    git_commit: str | None  # None outside a git checkout
    git_dirty: bool | None
    timestamp: str

    @classmethod
    def collect(cls) -> Metadata:
        jit = getattr(sys, "_jit", None)
        status = _git("status", "--porcelain")
        return cls(
            python=sys.version,
            platform=platform.platform(),
            jit_enabled=jit.is_enabled() if jit else None,
            git_commit=_git("rev-parse", "HEAD"),
            git_dirty=bool(status) if status is not None else None,
            timestamp=datetime.now(UTC).isoformat(),
        )


@dataclass(frozen=True)
class Report:
    problem: str
    budget: float
    repeat: int
    metadata: Metadata
    results: tuple[StrategyResult, ...]


def format_seconds(seconds: float) -> str:
    for limit, scale, unit in _UNITS:
        if seconds < limit:
            return f"{seconds * scale:.4g} {unit}"
    return f"{seconds:.4g} s"


def render_table(results: Sequence[StrategyResult]) -> str:
    """Rows are sizes, columns are strategies; growth goes in the last row."""
    sizes = sorted({m.size for r in results for m in r.measurements})
    medians = [{m.size: m.median for m in r.measurements} for r in results]

    rows = [["size", *(r.strategy for r in results)]]
    for size in sizes:
        cells = [format_seconds(t[size]) if size in t else "" for t in medians]
        rows.append([str(size), *cells])
    rows.append(["growth", *(str(r.growth) if r.growth else "-" for r in results)])

    widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]
    lines = []
    for row in rows:
        first, *rest = row
        cells = [first.rjust(widths[0])]
        cells += [cell.ljust(width) for cell, width in zip(rest, widths[1:])]
        lines.append("  ".join(cells).rstrip())
    return "\n".join(lines)


def write_json(report: Report, path: Path) -> None:
    path.write_text(json.dumps(asdict(report), indent=2) + "\n")
