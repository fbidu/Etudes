"""Compare the strategies of a problem, e.g. `python -m benchmarks fibonacci`."""

import argparse
import functools
import sys
from collections.abc import Sequence
from pathlib import Path

from benchmarks.fibonacci import FIBONACCI
from benchmarks.harness import (
    DEFAULT_REPEAT,
    StrategiesDisagree,
    check_agreement,
    measure,
    sweep,
)
from benchmarks.report import Metadata, Report, StrategyResult, render_table, write_json

PROBLEMS = {problem.name: problem for problem in (FIBONACCI,)}
DEFAULT_BUDGET = 0.25


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem", choices=PROBLEMS)
    parser.add_argument(
        "--strategy",
        action="append",
        help="strategy to run; repeat for several (default: all)",
    )
    parser.add_argument(
        "--budget",
        type=float,
        default=DEFAULT_BUDGET,
        help="stop a strategy after a call takes longer than this many seconds",
    )
    parser.add_argument("--repeat", type=int, default=DEFAULT_REPEAT)
    parser.add_argument("--json", type=Path, help="also save the results here")
    parser.add_argument(
        "--once",
        type=int,
        metavar="N",
        help="call each strategy once at size N without timing, e.g. to profile",
    )
    args = parser.parse_args(argv)

    problem = PROBLEMS[args.problem]
    names = [s.name for s in problem.strategies]
    unknown = set(args.strategy or ()) - set(names)
    if unknown:
        parser.error(
            f"unknown strategy {', '.join(sorted(unknown))}; choose from {', '.join(names)}"
        )
    strategies = [
        s for s in problem.strategies if not args.strategy or s.name in args.strategy
    ]

    if args.once is not None:
        data = problem.make_input(args.once)
        for strategy in strategies:
            strategy.factory()(data)
        return

    try:
        check_agreement(problem)
    except StrategiesDisagree as error:
        sys.exit(f"error: {error}")

    results = []
    for strategy in strategies:
        print(f"sweeping {strategy.name}...", file=sys.stderr)
        measurements = sweep(
            problem,
            strategy,
            args.budget,
            functools.partial(measure, repeat=args.repeat),
        )
        results.append(StrategyResult.from_sweep(strategy.name, measurements))
    print(render_table(results))

    if args.json:
        report = Report(
            problem=problem.name,
            budget=args.budget,
            repeat=args.repeat,
            metadata=Metadata.collect(),
            results=tuple(results),
        )
        write_json(report, args.json)
        print(f"saved {args.json}", file=sys.stderr)


if __name__ == "__main__":
    main()
