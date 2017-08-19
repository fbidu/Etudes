# encoding: utf-8
"""
Multiple binary search strategies in Python.

All the functions defined must return the
position of the key or -1 if not found.
In case of duplicates, any of the possible indexes are valid
"""
from random import randint

def simple_binary_search(array, start, key, offset=0):
    """
    A simple way to implement a binary search without using Python's
    bisect module.
    The offset is necessary because when we move to the right, the position
    of the elements in the sub array does not reflect their position in the
    original one. To fix this, when we call the function again for the right
    part of the array, we carry in the offset how many elements we left
    behind
    """
    # Did we hit the key?
    if array[start] == key:
        return start + offset
    # Did we expire the possibilities?
    elif start == 0:
        return -1
    # If the key is bigger than the current item, we go the left
    elif key > array[start]:
        right_array = array[start + 1:]
        mid = len(right_array) // 2
        offset += len(array) - len(right_array)
        return simple_binary_search(right_array, mid, key, offset)
    # If not, we go to the right
    else:
        left_array = array[:start]
        mid = len(left_array) // 2
        return simple_binary_search(left_array, mid, key, offset)

tests = 0
errors = 0
for t in range(50):
    size = randint(0, 9000)
    print('Test #{}. Array of size {}'.format(t, size))
    a = [randint(-1000, 1000) for _ in range(size)]
    a.sort()
    for index in range(len(a)):
        try:
            found = simple_binary_search(a, len(a) // 2, a[index])
            tests += 1
            assert a[index] == a[found]
        except AssertionError:
            errors += 1
            print('test #{}. Found: {}, original: {}'.format(t, found, index))
            print('array: {}'.format(a))

print('{} tests, {} errors'.format(tests, errors))
