"""Draw sweep results as an interactive log-log chart."""

import math
from collections.abc import Sequence
from pathlib import Path

import numpy as np
import plotly.graph_objects as go

from benchmarks.report import StrategyResult, format_seconds

# Categorical slots in their fixed, colour-blind-checked order (light mode)
SERIES = (
    "#2a78d6",
    "#eb6834",
    "#1baf7a",
    "#eda100",
    "#e87ba4",
    "#008300",
    "#6250d6",
    "#e34948",
)
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
FONT = 'system-ui, -apple-system, "Segoe UI", sans-serif'


def _label(result: StrategyResult) -> str:
    if result.growth is None:
        return result.strategy
    return f"{result.strategy} · {result.growth.fits[0].name}"


def _add_strategy(figure: go.Figure, result: StrategyResult, color: str) -> None:
    sizes = [m.size for m in result.measurements]
    medians = [m.median for m in result.measurements]
    if result.growth is not None:
        n = np.geomspace(sizes[0], sizes[-1], 200)
        figure.add_scatter(
            x=n,
            y=result.growth.fits[0].predict(n),
            mode="lines",
            line={"color": color, "width": 2},
            legendgroup=result.strategy,
            showlegend=False,
            hoverinfo="skip",
        )
    figure.add_scatter(
        x=sizes,
        y=medians,
        mode="markers",
        name=_label(result),
        legendgroup=result.strategy,
        marker={"color": color, "size": 10, "line": {"color": SURFACE, "width": 2}},
        customdata=[format_seconds(t) for t in medians],
        hovertemplate=f"{result.strategy}<br>n = %{{x}}<br>%{{customdata}}<extra></extra>",
    )
    # Log axes place annotations in log10 units
    figure.add_annotation(
        x=math.log10(sizes[-1]),
        y=math.log10(medians[-1]),
        text=_label(result),
        showarrow=False,
        xanchor="left",
        xshift=10,
        font={"color": INK_SECONDARY},
    )


def build_figure(
    problem: str, results: Sequence[StrategyResult], strategies: Sequence[str]
) -> go.Figure:
    """Chart median time per call against size, one colour per strategy.

    `strategies` lists all of the problem's strategies in order, so each
    keeps its colour when a run only includes some of them.
    """
    figure = go.Figure()
    for result in results:
        _add_strategy(figure, result, SERIES[strategies.index(result.strategy)])

    axis = {"type": "log", "gridcolor": GRID, "linecolor": AXIS, "zeroline": False}
    figure.update_layout(
        template="none",
        title={"text": f"{problem}: median time per call"},
        font={"family": FONT, "color": INK},
        paper_bgcolor=SURFACE,
        plot_bgcolor=SURFACE,
        xaxis={**axis, "title": {"text": "input size n"}},
        yaxis={
            **axis,
            "title": {"text": "time per call"},
            "tickformat": "~s",
            "ticksuffix": "s",
        },
        hovermode="closest",
        margin={"r": 200},
    )
    return figure


def write_plot(
    problem: str,
    results: Sequence[StrategyResult],
    strategies: Sequence[str],
    path: Path,
) -> None:
    """Write the chart as HTML that loads plotly.js from its CDN, to stay small."""
    build_figure(problem, results, strategies).write_html(path, include_plotlyjs="cdn")
