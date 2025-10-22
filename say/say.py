single_digit_words = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
two_digit_words = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}
special_digit_words = {
    **single_digit_words, 
    **two_digit_words, 
    **{
        11: "eleven", 
        12: "twelve", 
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }
}

# Larger scales
scales = [
    (1_000_000_000, "billion"),
    (1_000_000, "million"),
    (1_000, "thousand"),
    (100, "hundred"),
]

def say(number):
    if not (0 <= number < 1_000_000_000_000):
        raise ValueError("input out of range")
    if number in special_digit_words:
        return special_digit_words[number]
    
    for scale_value, scale_name in scales:
        if number >= scale_value:
            quotient, remainder = divmod(number, scale_value)
            if remainder == 0:
                return f"{say(quotient)} {scale_name}"
            return f"{say(quotient)} {scale_name} {say(remainder)}"
         
    if 20 <= number < 100:
        tens = (number // 10) * 10
        units = number % 10
        if units == 0:
            return special_digit_words[tens]
        return f"{special_digit_words[tens]}-{special_digit_words[units]}"

    return "unknown"
