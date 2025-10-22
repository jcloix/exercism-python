def classify(number):
    """
    A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    total = 1 if number > 1 else 0  # 1 is always a divisor (except for number=1)
    
    # only check up to sqrt(number)
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            total += i
            if i != number // i:   # avoid double-counting square roots
                total += number // i
    if total == number:
        return "perfect"
    elif total < number:
        return "deficient"
    else:
        return "abundant"
