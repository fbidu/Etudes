import math

import pytest

from benchmarks.harness import Measurement
from benchmarks.plot import SERIES, build_figure, spread
from benchmarks.report import StrategyResult

SIZES = [40, 100, 200, 400, 800, 1600]


def _linear_result(name: str, scale: float = 1.0) -> StrategyResult:
    measurements = tuple(
        Measurement(name, n, ((2e-7 + 1.4e-7 * n) * scale * (1.01 if i % 2 else 0.99),))
        for i, n in enumerate(SIZES)
    )
    return StrategyResult.from_sweep(name, measurements)


def _legend(figure) -> dict[str, str]:
    """Legend entry name -> marker colour."""
    return {t.name: t.marker.color for t in figure.data if t.showlegend is not False}


def test_plot_shows_every_strategy_with_its_growth():
    """The chart is for comparing strategies, so each one must appear,
    labelled with the shape its timings follow."""
    figure = build_figure(
        "demo", [_linear_result("fast"), _linear_result("slow")], ["fast", "slow"]
    )

    assert set(_legend(figure)) == {"fast · n", "slow · n"}


def test_a_strategy_keeps_its_colour_when_others_are_filtered_out():
    """Running with --strategy must not repaint the remaining strategies,
    or two charts of the same problem would disagree on who is who."""
    figure = build_figure("demo", [_linear_result("slow")], ["fast", "slow"])

    assert _legend(figure) == {"slow · n": SERIES[1]}


def test_labels_with_room_stay_at_their_line():
    """A label only moves to make room, so one that overlaps nothing keeps
    pointing at the end of its own line."""
    assert spread([3.0, 0.0, 1.0], gap=0.5) == [3.0, 0.0, 1.0]


def test_overlapping_labels_move_apart_around_their_middle():
    """Two strategies ending 15% apart drew their labels on top of each
    other. Moving both around their middle keeps each label beside its own
    line, and in the same order as the lines."""
    assert spread([1.1, 1.0], gap=0.5) == pytest.approx([1.3, 0.8])


def test_a_crowd_of_labels_is_spaced_as_one():
    """Making room for one pair can push a label into the next one, so the
    whole crowd must be spaced together."""
    heights = [0.0, 0.4, 0.8]
    # Sanity check: spreading only the first pair reaches the third label
    assert spread(heights[:2], gap=0.5)[1] + 0.5 > heights[2]

    assert spread(heights, gap=0.5) == pytest.approx([-0.1, 0.4, 0.9])


def test_chart_spreads_labels_of_strategies_ending_close_together():
    """The chart must actually use the spreading for its end labels."""
    figure = build_figure(
        "demo",
        [_linear_result("fast"), _linear_result("slow", scale=1.15)],
        ["fast", "slow"],
    )

    fast, slow = (annotation.y for annotation in figure.select_annotations())
    assert slow - fast > math.log10(1.15)
