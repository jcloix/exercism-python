all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotate(text, key):
    key = key % 26  # ensure 0–25
    rotated_lower = all_chars[key:26] + all_chars[:key]
    rotated_upper = all_chars[26+key:] + all_chars[26:26+key]
    rotate_map = str.maketrans(all_chars, rotated_lower + rotated_upper)
    return text.translate(rotate_map)