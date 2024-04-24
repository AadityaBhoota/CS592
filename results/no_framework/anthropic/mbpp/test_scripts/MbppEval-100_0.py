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

    # Find the length of the number
    n = len(num_str)

    # If the length is odd, we need to handle the middle digit separately
    if n % 2 == 1:
        middle = n // 2
        left = int(num_str[:middle])
        right = int(num_str[middle+1:][::-1])

        # If the middle digit is less than 9, we can just increment it
        if int(num_str[middle]) < 9:
            new_middle = str(int(num_str[middle]) + 1)
            return int(str(left) + new_middle + str(right))
        # If the middle digit is 9, we need to handle it differently
        else:
            new_left = left + 1
            new_right = 0
            return int(str(new_left) + "0" + str(new_right))
    # If the length is even, we can handle the left and right halves separately
    else:
        left = int(num_str[:n//2])
        right = int(num_str[n//2:][::-1])

        # If the right half is less than the left half, we can just increment the right half
        if right < left:
            new_right = right + 1
            return int(str(left) + str(new_right))
        # If the right half is greater than or equal to the left half, we need to increment the left half
        else:
            new_left = left + 1
            new_right = 0
            return int(str(new_left) + str(new_right) + str(new_right))

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)