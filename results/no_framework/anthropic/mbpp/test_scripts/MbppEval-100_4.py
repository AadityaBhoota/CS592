def next_smallest_palindrome(num):
    """
    Write a function to find the next smallest palindrome of a specified integer, returned as an integer.

    Examples:
    next_smallest_palindrome(99) == 101
    next_smallest_palindrome(1221) == 1331
    next_smallest_palindrome(120) == 121
    """
    num_str = str(num)
    length = len(num_str)

    # If the number is already a palindrome, return the next palindrome
    if num_str == num_str[::-1]:
        return num + 2

    # Find the middle point
    mid = length // 2

    # Construct the next palindrome
    left = num_str[:mid]
    right = num_str[mid:][::-1] if length % 2 == 0 else num_str[mid + 1:][::-1]

    next_palindrome = int(left + right)

    # If the original number is less than the next palindrome, return it
    if num < next_palindrome:
        return next_palindrome
    else:
        # Otherwise, increment the left part by 1 and construct the palindrome
        left_digit = int(left[0]) + 1
        left = str(left_digit) + left[1:]
        right = left[:-1][::-1]
        return int(left + right)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)