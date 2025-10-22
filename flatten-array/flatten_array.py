def flatten(iterable):
    result = []
    for element in iterable:
        if element is None:
            continue
        if isinstance(element, (list, tuple)):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result
