def square_root(number):
    return binary_search_sqrt(number, 0, number)


def binary_search_sqrt(target, low, high):
    if high < low:
        return None
    mid = round((low + high) / 2.0)
    if mid * mid == target:
        return mid
    elif mid * mid > target:
        return binary_search_sqrt(target, low, mid - 1)
    else:
        return binary_search_sqrt(target, mid + 1, high)
