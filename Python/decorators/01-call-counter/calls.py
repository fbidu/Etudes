import functools
import logging

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)

calls = 0


def record_calls(func):
    @functools.wraps(func)
    def decorate(*args):

        return func

    global calls
    calls += 1
    decorate.call_count = calls
    return decorate


@record_calls
def greet(name="Bidu"):
    print(f"Hey, {name}")


greet("world")

assert greet.call_count == 1

greet("Bidu")

# breakpoint
assert greet.call_count == 2
