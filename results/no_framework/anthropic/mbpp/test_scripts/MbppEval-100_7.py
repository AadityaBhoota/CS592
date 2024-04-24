def next_smallest_palindrome(num):
    """
    Find the next smallest palindrome of a given integer.

    Args:
        num (int): The input integer.

    Returns:
        int: The next smallest palindrome of the input integer.
    """
    num_str = str(num)
    length = len(num_str)

    # Handle the case when the input is already a palindrome
    if num_str == num_str[::-1]:
        return num

    # Construct the next palindrome
    middle = length // 2
    left_half = num_str[:middle]

    # If the number has an odd number of digits, the middle digit will be the same
    if length % 2 != 0:
        middle_digit = num_str[middle]
    else:
        middle_digit = ""

    # Construct the right half of the palindrome
    right_half = left_half[::-1]

    # Increment the left half if necessary
    if length % 2 != 0 and int(middle_digit) < 9:
        left_half = str(int(left_half) + 1)
        right_half = left_half[::-1]
    elif length % 2 == 0 and int(num_str[middle - 1]) < 9:
        left_half = str(int(left_half[:-1]) + 1) + left_half[-1]
        right_half = left_half[::-1]

    next_palindrome = left_half + middle_digit + right_half
    return int(next_palindrome)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)