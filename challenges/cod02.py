def from_base(arr):
    result = 0
    for idx, item in enumerate(arr):
        result += (-2) ** idx * item

    return result


def to_base(n):

    if n == 0:
        return [0]

    result = [1, 0]

    while n != 0:
        remainder = n % (-2)
        n = n // (-2)
        if remainder < 0:
            remainder += 2
            n += 1
        result.append(remainder)

    return result[::-1]
