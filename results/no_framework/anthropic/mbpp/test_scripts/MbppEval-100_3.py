def next_smallest_palindrome(num):
    """
    Find the next smallest palindrome of a specified integer, returned as an integer.

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

    # Construct the next palindrome
    middle = length // 2
    left_half = num_str[:middle]

    if length % 2 == 0:
        right_half = left_half[::-1]
    else:
        right_half = num_str[middle + 1:][::-1]

    next_palindrome = int(left_half + num_str[middle] + right_half)

    # If the original number is less than the next palindrome, return the next palindrome
    if num < next_palindrome:
        return next_palindrome
    else:
        return next_palindrome + 10 ** (length // 2)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)