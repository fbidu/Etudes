from collections.abc import Iterator


class Fibonacci:
    def __call__(self, n: int) -> int:
        raise NotImplementedError

    def iter(self, n: int) -> Iterator[int]:
        i = 0
        while i < n:
            yield self(i)
            i += 1


class BasicFib(Fibonacci):
    def __call__(self, n: int) -> int:
        if n < 2:
            return n
        return self(n - 2) + self(n - 1)


class MemoizedFib(Fibonacci):
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n: int) -> int:
        if n < len(self.cache):
            return self.cache[n]
        fib = self(n - 2) + self(n - 1)
        self.cache.append(fib)
        return fib


class TabulatedFib(Fibonacci):
    """MemoizedFib's table built bottom-up: a loop fills it from 0 to n
    instead of recursion filling it on the way back from n."""

    def __call__(self, n: int) -> int:
        table = []
        a, b = 0, 1
        for _ in range(n + 1):
            table.append(a)
            a, b = b, a + b
        return table[n]


class DictTabulatedFib(Fibonacci):
    """TabulatedFib with a dict as its table, keyed by position."""

    def __call__(self, n: int) -> int:
        table: dict[int, int] = {}
        a, b = 0, 1
        for i in range(n + 1):
            table[i] = a
            a, b = b, a + b
        return table[n]


STRATEGIES: tuple[type[Fibonacci], ...] = (
    BasicFib,
    MemoizedFib,
    TabulatedFib,
    DictTabulatedFib,
)
