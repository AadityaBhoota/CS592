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

    # Determine the length of the number
    length = len(num_str)

    # If the number is already a palindrome, return the number itself
    if num_str == num_str[::-1]:
        return num

    # Find the middle index of the number
    middle = length // 2

    # Initialize the left and right halves of the number
    left = num_str[:middle]
    right = num_str[middle:]

    # If the number is odd, handle the middle digit separately
    if length % 2 != 0:
        middle_digit = num_str[middle]

    # Construct the next smallest palindrome
    if num_str < left + left[::-1]:
        # If the number is smaller than its palindrome, increment the left half
        left = str(int(left) + 1)
        if length % 2 != 0:
            # If the number is odd, update the middle digit
            middle_digit = '0'
        right = left[::-1]
    else:
        # If the number is greater than or equal to its palindrome, decrement the left half
        left = str(int(left) - 1)
        if length % 2 != 0:
            # If the number is odd, update the middle digit
            middle_digit = '9'
        right = left[::-1]

    # Construct the final palindrome
    if length % 2 != 0:
        return int(left + middle_digit + right)
    else:
        return int(left + right)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)