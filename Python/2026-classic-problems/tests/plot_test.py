from benchmarks.harness import Measurement
from benchmarks.plot import SERIES, build_figure
from benchmarks.report import StrategyResult

SIZES = [40, 100, 200, 400, 800, 1600]


def _linear_result(name: str) -> StrategyResult:
    measurements = tuple(
        Measurement(name, n, ((2e-7 + 1.4e-7 * n) * (1.01 if i % 2 else 0.99),))
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
