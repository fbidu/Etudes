from classic.fibonacci import basic_fib

strategies = [basic_fib]


def benchmark_fib_calls():
    for strategy in strategies:
        strategy(40)


if __name__ == "__main__":
    benchmark_fib_calls()
