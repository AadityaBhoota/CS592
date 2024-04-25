def next_smallest_palindrome(num):
    """
    Write a function to find the next smallest palindrome of a specified integer, returned as an integer.

    Examples:
    next_smallest_palindrome(99) == 101
    next_smallest_palindrome(1221) == 1331
    next_smallest_palindrome(120) == 121
    """
    # Convert the input number to a string
    num_str = str(num)

    # Check if the number is already a palindrome
    if num_str == num_str[::-1]:
        return num

    # Find the length of the number
    n = len(num_str)

    # Initialize the middle digit
    mid = n // 2

    # If the number of digits is odd, copy the middle digit
    if n % 2 != 0:
        left_part = int(num_str[:mid])
        right_part = int(num_str[mid+1:][::-1])
    # If the number of digits is even, copy the middle two digits
    else:
        left_part = int(num_str[:mid])
        right_part = int(num_str[mid:][::-1])

    # Calculate the next palindrome
    next_palindrome = int(str(left_part) + str(right_part))

    # If the original number is less than the next palindrome, return it
    if num < next_palindrome:
        return next_palindrome
    # Otherwise, increment the left part and recalculate the palindrome
    else:
        left_part += 1
        right_part = int(str(left_part)[::-1])
        return int(str(left_part) + str(right_part))

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)