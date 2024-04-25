def next_smallest_palindrome(num):
    """
    Finds the next smallest palindrome of a given integer.

    Args:
        num (int): The input integer.

    Returns:
        int: The next smallest palindrome of the input integer.
    """
    num_str = str(num)
    length = len(num_str)

    # If the number is already a palindrome, return it
    if num_str == num_str[::-1]:
        return num

    # Determine the middle index
    mid = length // 2

    # Extract the left and right halves of the number
    left = num_str[:mid]
    right = num_str[mid:]

    # If the number is odd, copy the middle digit to the right half
    if length % 2 == 1:
        right = num_str[mid + 1:]

    # Convert the left and right halves to integers
    left_int = int(left)
    right_int = int(right[::-1])

    # Compute the next smallest palindrome
    if left_int < right_int:
        next_palindrome = int(left + right[::-1])
    else:
        carry = 1
        left_int += carry
        left = str(left_int)
        next_palindrome = int(left + right[::-1])

    return next_palindrome

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)