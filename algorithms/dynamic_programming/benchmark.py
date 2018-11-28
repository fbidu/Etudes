from time import perf_counter


def benchmark(function, arguments, calls, add_iteraction=True):
    """
    A simple benchmarking function.

    It accepts a function and a list of arguments an iterator
    for the calls - something like range(1, 10) and wether
    or not it should add the current iteration step as
    an last argument.
    """
    prev_time = 0
    ratio = 0
    for i in calls:
        init = perf_counter()

        if add_iteraction:
            function(*arguments, i)
        else:
            function(*arguments)

        final = perf_counter()
        curr_time = final - init

        if prev_time:
            ratio = (curr_time / prev_time) * 100

        prev_time = curr_time
        print(
            "i={0:d} took {1:.4f}s - {2:.1f}% more than the last".format(
                i, curr_time, ratio
            )
        )
