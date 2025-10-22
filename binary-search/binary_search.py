def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")
    return find_recursive(search_list, value, 0, len(search_list) - 1)

def find_recursive(search_list, value, low, high):
    if low > high:
        raise ValueError("value not in array")
    mid = (low + high) // 2
    if search_list[mid] == value:
        return mid
    elif search_list[mid] < value:
        return find_recursive(search_list, value, mid + 1, high)
    else:
        return find_recursive(search_list, value, low, mid - 1)     