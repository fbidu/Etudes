import json
import sys

import pytest

from benchmarks.growth import Candidate, Fit, Growth, Term
from benchmarks.harness import Measurement
from benchmarks.report import (
    Metadata,
    Report,
    StrategyResult,
    format_seconds,
    render_table,
    write_json,
)


def _exponential_growth() -> Growth:
    fit = Fit(Candidate("b^n", (Term.EXPONENTIAL,)), (0.0, 1e-7), 1.618, -50.0)
    return Growth((fit,))


def _result(name: str, seconds_by_size: dict[int, float]) -> StrategyResult:
    return StrategyResult(
        strategy=name,
        measurements=tuple(
            Measurement(name, size, (seconds,))
            for size, seconds in seconds_by_size.items()
        ),
        growth=None,
    )


def test_table_leaves_sizes_past_budget_blank():
    """A strategy that hit the budget has no timing at larger sizes. The
    cell stays empty instead of showing a number that was never measured."""
    slow = _result("slow", {5: 1e-3, 10: 1.0})
    fast = _result("fast", {5: 1e-6, 10: 2e-6, 20: 4e-6})

    table = render_table([slow, fast])

    row = next(line for line in table.splitlines() if line.lstrip().startswith("20"))
    assert row.split() == ["20", "4", "µs"]


def test_table_shows_each_strategys_growth():
    """The growth estimate is the headline of a sweep, so it sits under
    each strategy's column."""
    linear = Fit(Candidate("n", (Term.N,)), (1e-7, 1e-9), None, -90.0)
    basic = StrategyResult("basic", (), _exponential_growth())
    memoized = StrategyResult("memoized", (), Growth((linear,)))

    table = render_table([basic, memoized])

    growth_row = table.splitlines()[-1]
    assert str(basic.growth) in growth_row
    assert str(memoized.growth) in growth_row


@pytest.mark.parametrize(
    ("seconds", "expected"),
    [
        (3.2e-7, "320 ns"),
        (1.5e-5, "15 µs"),
        (0.0123, "12.3 ms"),
        (1.234, "1.234 s"),
    ],
)
def test_times_use_a_readable_unit(seconds, expected):
    """Timings span nanoseconds to seconds across strategies; raw floats
    in seconds would be unreadable side by side."""
    assert format_seconds(seconds) == expected


def test_metadata_records_the_running_interpreter():
    """Results only compare across runs when each run says which Python
    produced it."""
    metadata = Metadata.collect()

    assert metadata.python == sys.version


def test_json_report_keeps_samples_and_metadata(tmp_path):
    """Saved results are for comparing later runs, so they keep the raw
    samples and the environment, not only the medians shown on screen."""
    # Setup
    result = StrategyResult(
        strategy="basic",
        measurements=(Measurement("basic", 5, (1e-3, 2e-3)),),
        growth=_exponential_growth(),
    )
    report = Report(
        problem="fibonacci",
        budget=0.25,
        repeat=2,
        metadata=Metadata.collect(),
        results=(result,),
    )
    path = tmp_path / "results.json"

    # Act
    write_json(report, path)

    # Assert
    saved = json.loads(path.read_text())
    assert saved["problem"] == "fibonacci"
    assert saved["metadata"]["python"] == sys.version
    assert saved["results"][0]["measurements"][0]["samples"] == [1e-3, 2e-3]
    best = saved["results"][0]["growth"]["fits"][0]
    assert best["candidate"] == {"name": "b^n", "terms": ["b^n"]}
    assert best["base"] == 1.618
