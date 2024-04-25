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

    # Construct the next palindrome
    mid = length // 2
    left = num_str[:mid]
    right = num_str[mid:][::-1] if length % 2 == 0 else num_str[mid + 1:][::-1]

    new_num = int(left + right)

    # If the new number is still smaller than the original number, increment it
    if new_num <= num:
        new_num += 10 ** (length - (length % 2))

    return new_num

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)