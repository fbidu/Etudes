import random
from itertools import combinations
from quick_find import QuickFind


def main(length=5000):
    qf = QuickFind(length)

    pairs = list(combinations(range(length), 2))

    unions = random.sample(pairs, length // 2) 
    queries = random.sample(pairs, length // 2) 

    for u in unions:
        qf.union(*u)

    for u in unions:
        qf.connected(*u)


if __name__ == "__main__":
    main()
