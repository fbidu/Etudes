# coding: utf-8


def urlify(string):
    """
    This function replaces all space characters on a string for %20
    """
    string = list(string)

    while string.count(' '):
        string[string.index(' ')] = '%20'

    return ''.join(string)


def test_urlify():
    assert urlify('felipe videira rodrigues') == 'felipe%20videira%20rodrigues'
    assert urlify('  ') == '%20%20'
    assert urlify(' a ') == '%20a%20'
    assert urlify('a   b') == 'a%20%20%20b'

print(urlify('blablabla'))
print(urlify('a   b   c   d'))
print(urlify(' a b c '))
