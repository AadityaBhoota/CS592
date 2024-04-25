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

    # If the length is odd, find the middle digit and increment it by 1 if it's not 9
    if length % 2 == 1:
        middle = length // 2
        if num_str[middle] != '9':
            num_str = num_str[:middle] + str(int(num_str[middle]) + 1) + num_str[middle+1:]
        else:
            num_str = num_str[:middle] + '0' + num_str[middle+1:]
    # If the length is even, find the middle two digits and increment the right digit by 1 if it's not 9
    else:
        middle = length // 2 - 1
        if num_str[middle+1] != '9':
            num_str = num_str[:middle+1] + str(int(num_str[middle+1]) + 1) + num_str[middle+2:]
        else:
            num_str = num_str[:middle+1] + '0' + num_str[middle+2:]

    # Construct the new number by mirroring the left half to the right half
    left_half = num_str[:length//2]
    if length % 2 == 1:
        return int(num_str[:middle+1] + left_half[::-1])
    else:
        return int(left_half + left_half[::-1])

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)