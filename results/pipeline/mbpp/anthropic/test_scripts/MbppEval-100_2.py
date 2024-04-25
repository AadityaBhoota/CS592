import sys

def next_smallest_palindrome(num):
    '''
    Write a function to find the next smallest palindrome of a specified integer, returned as an integer.

    Examples:
    next_smallest_palindrome(99) == 101
    next_smallest_palindrome(1221) == 1331
    next_smallest_palindrome(120) == 121
    '''
    # Convert the input to a string
    num_str = str(num)
    
    # Check if the number is already a palindrome
    if num_str == num_str[::-1]:
        # If it is, return the next odd palindrome
        return num + 2
    
    # Find the middle index
    middle = len(num_str) // 2
    
    # Construct the next palindrome
    left_half = num_str[:middle]
    if len(num_str) % 2 == 0:
        right_half = num_str[middle:]
    else:
        right_half = num_str[middle+1:]
    
    next_palindrome_str = left_half + right_half[::-1]
    
    # Convert the result back to an integer and return it
    return int(next_palindrome_str)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)