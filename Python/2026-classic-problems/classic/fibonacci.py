from collections.abc import Iterator


class Fibonacci:
    def __call__(self, n: int) -> int:
        raise NotImplementedError

    def iter(self, n: int) -> Iterator[int]:
        raise NotImplementedError


class BasicFib(Fibonacci):
    def __call__(self, n: int) -> int:
        if n < 2:
            return n
        return self(n - 2) + self(n - 1)

    def iter(self, n: int) -> Iterator[int]:
        i = 0
        while i < n:
            yield self(i)
            i += 1


basic_fib = BasicFib()
