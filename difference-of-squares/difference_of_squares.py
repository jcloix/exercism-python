def square_of_sum(number):
    sum_value = sum(range(1, number + 1))
    return sum_value * sum_value


def sum_of_squares(number):
    total = sum(i * i for i in range(1, number + 1))
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
