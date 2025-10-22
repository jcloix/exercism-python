def append(list1, list2):
    result = []
    result.extend(list1)
    result.extend(list2)
    return result


def concat(lists):
    return [element for lst in lists for element in lst]


def filter(function, list):
    return [element for element in list if function(element)]


def length(list):
    return sum(1 for _ in list)


def map(function, list):
    return [function(element) for element in list]



def foldl(function, list, initial):
    for element in list:
        initial = function(initial, element)
    return initial


def foldr(function, list, initial):
    acc = initial
    for x in reversed(list):
        acc = function(acc, x)
    return acc


def reverse(list):
    return list[::-1]
