from array_list import ArrayList

def test_creation():
    a = ArrayList()
    assert str(a) == ''


def test_repeated_insertion():
    a = ArrayList()
    for _ in range(10):
        a.append(0)

    assert str(a) == '0, 0, 0, 0, 0, 0, 0, 0, 0, 0'


def test_a_little_bigger():
    a = ArrayList()
    base = ['3' for _ in range(15)]

    for _ in range(15):
        a.append(3)

    assert str(a) == ', '.join(base)


def test_long_insertion():
    a = ArrayList()
    base = ['3' for _ in range(1000)]

    for _ in range(1000):
        a.append(3)

    assert str(a) == ', '.join(base)
