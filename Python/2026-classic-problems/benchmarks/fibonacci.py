from benchmarks.harness import Problem, Strategy
from classic.fibonacci import STRATEGIES

# A cold MemoizedFib recurses about n/2 deep, so sizes stay below twice
# the default recursion limit of 1000.
FIBONACCI: Problem[int, int] = Problem(
    name="fibonacci",
    strategies=tuple(Strategy(cls.__name__, cls) for cls in STRATEGIES),
    make_input=lambda n: n,
    sizes=(5, 10, 15, 20, 25, 30, 35, 40, 100, 200, 400, 800, 1600),
    check_sizes=tuple(range(25)),
)
