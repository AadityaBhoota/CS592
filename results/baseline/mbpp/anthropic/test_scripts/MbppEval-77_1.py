def is_Diff(n):
    """
    Determine whether a number is divisible by 11.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is divisible by 11, False otherwise.
    """
    # Convert the number to a string
    num_str = str(n)

    # Initialize the difference
    diff = 0

    # Iterate through the digits of the number
    for i, digit in enumerate(num_str):
        # Add the digit if the index is even, subtract it if the index is odd
        if i % 2 == 0:
            diff += int(digit)
        else:
            diff -= int(digit)

    # Check if the difference is divisible by 11
    return diff % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)