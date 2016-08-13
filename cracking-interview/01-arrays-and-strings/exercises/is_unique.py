from collections import Counter


def is_unique(string):
    """
    Function that determines if a string is made of unique characters
    """
    # Creating a Counter based on the characters of the string
    c = Counter(list(string))
    # If the sum of the frequencies of the characters is equal to the number
    # of characters, every character is unique
    return sum(c.values()) == len(c.keys())

print(is_unique('felipe'))
print(is_unique('abcde'))
print(is_unique('aabbccdd'))


def is_unique_plain(string):
    """
    Function that determines if every character is unique
    without using additional data structures
    """
    # We'll loop through all the chars
    for i in range(len(string)):
        current_char = string[i]  # Getting the current char

        # Searching for the current char in the rest of the string. If we find
        # it, the char is not unique
        if string.find(current_char, i + 1) != -1:
            return False

    return True

print(is_unique_plain('felipe'))
print(is_unique_plain('abcde'))
print(is_unique_plain('aabbccdd'))

