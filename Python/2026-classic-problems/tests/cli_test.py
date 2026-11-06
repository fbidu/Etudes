import json
import subprocess
import sys
from pathlib import Path

import pytest

from benchmarks.__main__ import main
from benchmarks.fibonacci import FIBONACCI

PROJECT_ROOT = Path(__file__).parent.parent


def test_cli_compares_every_strategy_and_saves_json(tmp_path):
    """The command people run must time, report and plot every strategy end
    to end. A tiny budget stops each sweep after its first size so the
    test stays fast."""
    path = tmp_path / "fibonacci.json"
    plot = tmp_path / "fibonacci.html"
    strategies = [s.name for s in FIBONACCI.strategies]

    completed = subprocess.run(
        [sys.executable, "-m", "benchmarks", "fibonacci"]
        + ["--budget", "1e-9", "--repeat", "1", "--json", str(path)]
        + ["--plot", str(plot)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    header = completed.stdout.splitlines()[0]
    assert header.split() == ["size", *strategies]
    saved = json.loads(path.read_text())
    assert [r["strategy"] for r in saved["results"]] == strategies
    assert all(len(r["measurements"]) == 1 for r in saved["results"])
    assert "plotly" in plot.read_text()


def test_unknown_strategy_is_rejected():
    """A typo in --strategy must fail loudly instead of silently timing
    nothing."""
    with pytest.raises(SystemExit) as caught:
        main(["fibonacci", "--strategy", "NoSuchFib"])

    assert caught.value.code == 2
