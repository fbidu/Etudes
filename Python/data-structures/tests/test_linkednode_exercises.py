import linkednode
import linkednode_exercises


def test_remove_duplicates():
    middle = linkednode.LinkedNode(10)
    middle += 30
    middle += 40
    middle += 50
    middle += 50
    middle += 50
    middle += 50
    middle += 60
    middle = linkednode_exercises.remove_duplicates(middle)
    assert linkednode.print_list(middle) == '10, 30, 40, 50, 60'

    beginning = linkednode.LinkedNode(10)
    beginning += 10
    beginning += 10
    beginning += 10
    beginning += 20
    beginning += 30
    beginning = linkednode_exercises.remove_duplicates(beginning)
    assert linkednode.print_list(beginning) == '10, 20, 30'

    ending = linkednode.LinkedNode(10)
    ending += 20
    ending += 30
    ending += 30
    ending = linkednode_exercises.remove_duplicates(beginning)
    assert linkednode.print_list(ending) == '10, 20, 30'

    jumpy = linkednode.LinkedNode(1)
    jumpy += 2
    jumpy += 1
    jumpy += 2
    jumpy += 3
    jumpy += 1
    jumpy = linkednode_exercises.remove_duplicates(jumpy)
    assert linkednode.print_list(jumpy) == '1, 2, 3'

    mess = linkednode.LinkedNode(10)
    mess += 10
    mess += 10
    mess += 20
    mess += 30
    mess += 30
    mess += 40
    mess += 50
    mess += 10
    mess += 60
    mess += 60
    mess += 30
    mess = linkednode_exercises.remove_duplicates(mess)
    assert linkednode.print_list(mess) == '10, 20, 30, 40, 50, 60'