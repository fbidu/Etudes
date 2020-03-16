# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import namedtuple

from extratypes import Tree  # library with types used in the task

PerfectResult = namedtuple("PerfectResult", ["is_perfect", "height", "root"])


def find_perfect(root):
    if not root:
        # Empty entities are "perfect"
        return True

    left = find_perfect(root.l)
    right = find_perfect(root.r)

    if left.is_perfect and right.is_perfect and left.height == right.height:
        return PerfectResult(True, left.height + 1, root)

    max_subtree = max(left.height, right.height)
    if max_subtree == left.height:
        max_root = left.root
    else:
        max_root = right.root

    return PerfectResult(False, max_subtree, max_root)


def solution(T):
    # write your code in Python 3.6
    return find_perfect(T)
