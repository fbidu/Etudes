from collections import Counter


def check_permutation(first_string, second_string):

    if len(first_string) != len(second_string):
        return False

    first_counter = Counter(list(first_string))
    second_counter = Counter(list(second_string))

    for key in first_counter:
        if first_counter[key] != second_counter[key]:
            return False

    return True

print(check_permutation('abc', 'bca'))
print(check_permutation('felipe', 'lefipe'))
print(check_permutation('batata', 'felipe'))
