from collections import deque

def is_paired(input_string):
    stack = deque()
    opening = "([{"
    closing = ")]}"
    matches = {')': '(', ']': '[', '}': '{'}
    for char in input_string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != matches[char]:
                return False
    return not stack
