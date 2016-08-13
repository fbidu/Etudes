from _pytest.python import NoneType

from linkednode import LinkedNode, print_list, delete_item


def test_create_empty():
    list = LinkedNode(10)
    assert list.key == 10


def test_insert():
    list = LinkedNode(10)
    list += 30
    list += 40
    list += 50
    assert repr(list) == '10'
    assert repr(list.next_node.key) == '30'
    assert print_list(list) == '10, 30, 40, 50'


def test_delete():
    list = LinkedNode(10)
    list += 20
    list += 30
    list += 40
    list = delete_item(list, 30)
    assert print_list(list) == '10, 20, 40'

    list = delete_item(list, 10)
    assert print_list(list) == '20, 40'

    list = delete_item(list, 50)
    assert print_list(list) == '20, 40'

    list = delete_item(list, 40)
    assert print_list(list) == '20'

    list = delete_item(list, 20)
    assert type(list) == NoneType
