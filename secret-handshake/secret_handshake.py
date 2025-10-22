actions = ["wink", "double blink", "close your eyes", "jump"]
def commands(binary_str):
    if not binary_str:
        return []

    result = [actions[i] for i,l in enumerate(reversed(binary_str[1:])) if l == '1']
    if binary_str[0] == '1':
        result.reverse()
    return result
