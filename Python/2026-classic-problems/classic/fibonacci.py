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


STRATEGIES: tuple[type[Fibonacci], ...] = (BasicFib, MemoizedFib)
