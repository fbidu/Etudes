import argparse

from classic.fibonacci import basic_fib, memoized_fib

strategies = [basic_fib, memoized_fib]


def benchmark_fib_calls():
    for strategy in strategies:
        strategy(40)


def benchmark_fib_call(strategy, iterations=40):
    strategy(iterations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark Fibonacci implementations")
    parser.add_argument(
        "--strategy",
        choices=["basic", "memoized"],
        help="Fibonacci strategy to benchmark",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=40,
        help="Number of iterations to run the benchmark",
    )
    args = parser.parse_args()
    strategy = args.strategy if args.strategy else None
    iterations = args.iterations
    if strategy == "basic":
        benchmark_fib_call(basic_fib, iterations)
    elif strategy == "memoized":
        benchmark_fib_call(memoized_fib, iterations)
    else:
        benchmark_fib_calls()
