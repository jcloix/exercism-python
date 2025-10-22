def is_valid(isbn):
    cleaned_isbn = isbn.replace("-", "").replace(" ", "")
    if len(cleaned_isbn) != 10 or not cleaned_isbn[:-1].isdigit() or (cleaned_isbn[-1] not in "0123456789X"):
        return False
        
    total = sum(int(digit) * (10 - idx) for idx, digit in enumerate(cleaned_isbn[:-1]))
    if cleaned_isbn[-1] == "X":
        total += 10
    else:
        total += int(cleaned_isbn[-1])

    return total % 11 == 0
