def is_armstrong_number(number):
    
    """Check if a number is an Armstrong number."""
    num_str = str(number)
    length = len(num_str)
    return sum(int(digit) ** length for digit in num_str) == number
