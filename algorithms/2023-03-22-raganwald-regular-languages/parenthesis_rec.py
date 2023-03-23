"""
Recognizes if a given string has balanced parenthesis.
"""

from collections import deque


def valid(input_):
    q = deque()
    for char in input_:
        if char == "(":
            q.append(char)
        elif char == ")":
            if not q or q.pop() != "(":
                return False
        else:
            return False
    return not q


if __name__ == "__main__":
    print(valid("()"))
    print(valid(")("))
    print(valid("()()"))
    print(valid("(()())"))
    print(valid("(()))"))
