class LinkedNode:

    def __init__(self, k):
        self.key = k
        self.next_node = None

    def __iadd__(self, d):
        current_node = self
        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = LinkedNode(d)
        return self

    def __repr__(self):
        return str(self.key)

    def __str__(self):
        return str(self.key)


def print_list(list):
    items = []
    current_node = list

    while current_node:
        items.append(str(current_node))
        current_node = current_node.next_node

    return ', '.join(items)


def delete_item(list, key):
    current_node = list

    if current_node.key == key:
        list = list.next_node
        del current_node
        return list

    while current_node.next_node:
        if current_node.next_node.key == key:
            target_node = current_node.next_node
            current_node.next_node = target_node.next_node
            del target_node
            break
        current_node = current_node.next_node

    return list
