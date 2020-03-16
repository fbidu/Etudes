from math import ceil, sqrt

def trial_primality(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def trial_primality_squared(n):

    max_divisor = ceil(sqrt(n))
    for i in range(2, max_divisor):
        if n % i == 0:
            return False

    return True
