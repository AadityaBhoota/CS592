def is_Diff(n):
    """
    Determine whether a number is divisible by 11.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is divisible by 11, False otherwise.
    """
    # Convert the number to a string
    num_str = str(n)

    # Initialize the sum of the digits in the odd and even positions
    odd_sum = 0
    even_sum = 0

    # Iterate through the digits, adding them to the appropriate sum
    for i, digit in enumerate(num_str):
        if i % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    # Check if the difference between the sums is divisible by 11
    return (odd_sum - even_sum) % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)