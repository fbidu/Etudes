import re


def encode_timeslot(time_string):
    """
    takes an string in the format Wed 04:25 and returns its position
    in a list indexing every minute in a week.

    >>> encode_timeslot("Mon 00:00")
    0

    >>> encode_timeslot("Mon 00:01")
    1

    >>> encode_timeslot("Mon 01:00")
    60

    >>> encode_timeslot("Mon 23:59")
    1439

    >>> encode_timeslot("Tue 00:00")
    1440
    """
    pattern = re.compile(r"(\w{3}) (\d{2}):(\d{2})")

    days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    matches = re.findall(pattern, time_string)

    if not matches:
        raise Exception(f"'{time_string} is not in a valid format")

    day, hour, mins = matches[0]

    if not day in days:
        raise Exception(f"'{day} is not a valid day")

    day_index = days.index(day)
    hour = int(hour)
    mins = int(mins)

    return (hour * 60 + mins) + day_index * 1440


def find_longest_length(list_, target=0):
    """
    given a list of integers, finds the longest sequence
    of a target number, defaulting to 0

    >>> find_longest_length([0, 0, 0, 0])
    4

    >>> find_longest_length([])
    0

    >>> find_longest_length([0, 0, 0, 1])
    3

    >>> find_longest_length([1, 0, 0, 0])
    3

    >>> find_longest_length([0, 1, 1, 0])
    1

    >>> find_longest_length([1, 1, 1, 1])
    0
    """

    if not list_:
        return 0

    longest_match = 0
    current_match = 0

    for idx, item in enumerate(list_):

        # If we find an item, we increment the current match
        if item == target:
            current_match += 1

        # If we find somthing different then a target
        # and we're current matching, we need to process it
        if idx == len(list_) - 1 or item != target and current_match:
            if current_match > longest_match:
                longest_match = current_match

            current_match = 0

    return longest_match
