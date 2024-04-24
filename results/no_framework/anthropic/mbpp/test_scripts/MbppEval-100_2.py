import sys

def next_smallest_palindrome(num):
    """
    Write a function to find the next smallest palindrome of a specified integer, returned as an integer.

    Examples:
    next_smallest_palindrome(99) == 101
    next_smallest_palindrome(1221) == 1331
    next_smallest_palindrome(120) == 121
    """
    # Convert the number to a string
    num_str = str(num)

    # Check if the number is already a palindrome
    if num_str == num_str[::-1]:
        return num

    # Compute the length of the number
    length = len(num_str)

    # Compute the middle index of the number
    middle = length // 2

    # Initialize the new palindrome
    new_palindrome = ""

    # Construct the new palindrome
    for i in range(middle):
        new_palindrome += num_str[i]

    # If the length is odd, copy the middle digit
    if length % 2 == 1:
        new_palindrome += num_str[middle]

    # Reverse the first half and append it to the second half
    new_palindrome += new_palindrome[::-1]

    # Convert the new palindrome to an integer and return it
    return int(new_palindrome)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)