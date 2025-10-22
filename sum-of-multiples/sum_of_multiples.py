def sum_of_multiples(limit, multiples):
    return sum(n for n in range(limit) if any( m != 0 and n % m == 0 for m in multiples))
