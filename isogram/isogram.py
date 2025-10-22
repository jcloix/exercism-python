def is_isogram(string):
    cleaned = string.replace("-", "").replace(" ", "").lower()
    if len(cleaned) != len(set(cleaned)):
        return False
    return True
