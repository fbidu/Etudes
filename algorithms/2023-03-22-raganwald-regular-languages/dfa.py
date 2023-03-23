"""
Late night, tired DFA implementation.
"""
from __future__ import annotations


class DFA:
    begin: Node

    def accepts(self, input):
        node = self.begin
        step = 0
        while node and not node.final and step < len(input):
            if input[step] != node.accepts:
                return False
            # node = node sibling, etc

        if node.final:
            return True
        return False


class Node:
    def __init__(self, value, accepts: str, final: bool = False):
        self.value = value
        self.accepts = accepts
        self.final = final


if __name__ == "__main__":
    dfa = DFA()
    b_node = Node("B", accepts="I", final=True)

    dfa.begin = b_node

    print(dfa.accepts("B"))
    print(dfa.accepts("B"))
