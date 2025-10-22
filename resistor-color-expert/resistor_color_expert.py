color_codes = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
    "gold": -1,
    "silver": -2,
}
tolerance_code = {
    "brown": 1,
    "red": 2,
    "green": 0.5,
    "blue": 0.25,
    "violet": 0.1,
    "grey": 0.05,
    "gold": 5,
    "silver": 10,
}

def resistor_label(colors):
    if len(colors) == 1:
        return f"{color_codes[colors[0]]} ohms"
    total = sum(color_codes[color] * (10 ** i) for i, color in enumerate(reversed(colors[:-2]))) * (10 ** color_codes[colors[-2]])
    tolerance = tolerance_code[colors[-1]]
    if total >= 1_000_000_000:
        return f"{format_number(total / 1_000_000_000)} gigaohms ±{tolerance}%"
    elif total >= 1_000_000:
        return f"{format_number(total / 1_000_000)} megaohms ±{tolerance}%"
    elif total >= 1_000:
        return f"{format_number(total / 1_000)} kiloohms ±{tolerance}%"
    else:
        return f"{total} ohms ±{tolerance}%"


def format_number(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value