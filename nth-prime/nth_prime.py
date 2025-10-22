import math


def prime(number):
    """Returns the nth prime number."""
    if number < 1:
        raise ValueError("there is no zeroth prime")
    count = 0
    candidate = 1
    while count < number:
        candidate += 1
        for i in range(2, math.isqrt(candidate) + 1):
            if candidate % i == 0:
                break
        else:
            count += 1
    return candidate
