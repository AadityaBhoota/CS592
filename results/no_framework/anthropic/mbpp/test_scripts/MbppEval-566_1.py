def sum_digits(n):
    """
    Write a function to get the sum of the digits of a non-negative integer.

    Examples:
    sum_digits(345) == 12
    sum_digits(12) == 3
    sum_digits(97) == 16
    """
    # Convert the number to a string and then to a list of digits
    digits = [int(digit) for digit in str(n)]
    
    # Calculate the sum of the digits
    return sum(digits)

def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)