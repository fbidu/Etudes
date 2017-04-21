# coding: utf-8
"""
This module provides a function that checks if a
string is a permutation of a palindrome
"""
from collections import Counter


def palindrome_permutation(string):
    """
    Function that checks if a string is a palindrome's permutation.
    The logic here is split in two cases:
        * If the string is even sized, every letter must occur at
        even frequencies so that we can arrange them equaly in both halfs
        of the string
        * On the other hand, if the string is odd sized we need to have one
        and only one odd-frequent letter that acts as the 'middle' of the
        palindrome
    By the properties of the sum of odd and even numbers, we know for sure that
    inside an odd sized string, at least one character is odd-frequent.
    """
    # Normalizing the string by making it lower case and removing spaces
    string = string.lower().replace(' ', '')

    # Creating a frequency dictionary from the string's letters
    counter = Counter(list(string))

    # If the string is odd sized, there can be only one odd-frequency letter
    # so we start this flag with False in this case. If the string is even
    # sized, there can be no odd frequency letters so we start this flag as
    # true.
    has_odd_letter_occured = bool(len(string) % 2 == 0)

    # Looping through the string's unique characters
    for key in counter:

        # Getting that char's frequency
        frequency = counter[key]

        # Creating a flag to check the frequency's parity
        odd_frequency = frequency % 2 == 1

        # If the frequency is odd and we already have and odd-frequent letter,
        # we cannot make a palindrome out of it. Keep in mind that if the
        # string is even sized there can be NO odd frequent letters, that's
        # why in that case, I had already initialized this flag as True
        if odd_frequency and has_odd_letter_occured:
            return False
        elif not has_odd_letter_occured and odd_frequency:
            # If we don't have and odd frequent letter, we do now. Flagging it
            has_odd_letter_occured = True

    # If the loop did not return False, the string is a palindrome permutation
    return True

def test_palindrome_permutation():
    assert palindrome_permutation('Tact Coa')
    assert palindrome_permutation('aab')
    assert palindrome_permutation('aaaba')
    assert palindrome_permutation('baaab')
    assert not palindrome_permutation('baaabccc')
    assert not palindrome_permutation('felipe')
    assert not palindrome_permutation('python')

def palindrome_permutation_stack():
    """
    This function checks if a string is a palindrome permutation using a stack
    structure
    """

