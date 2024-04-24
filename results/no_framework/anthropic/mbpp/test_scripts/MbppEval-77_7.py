def is_Diff(n):
    """
    Determines whether a number is divisible by 11.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is divisible by 11, False otherwise.
    """
    # Convert the number to a string
    num_str = str(n)

    # Initialize the sum of alternate digits
    alt_sum = 0

    # Iterate through the digits, adding alternate digits
    for i, digit in enumerate(num_str):
        if i % 2 == 0:
            alt_sum += int(digit)
        else:
            alt_sum -= int(digit)

    # Check if the sum of alternate digits is divisible by 11
    return alt_sum % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)