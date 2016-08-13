import linkednode


def remove_duplicates(target_list):
    """
    Function that removes duplicates from a linked list
    """
    current_node = target_list
    while current_node:
        runner = current_node
        while runner.next_node:
            if runner.next_node.key == current_node.key:
                runner.next_node = linkednode.delete_item(runner.next_node,
                                                          current_node.key)
            else:
                runner = runner.next_node
        current_node = current_node.next_node
    return target_list
