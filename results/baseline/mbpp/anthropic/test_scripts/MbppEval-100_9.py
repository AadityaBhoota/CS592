def next_smallest_palindrome(num):
    """
    Find the next smallest palindrome of a specified integer.

    Args:
        num (int): The input integer.

    Returns:
        int: The next smallest palindrome of the input integer.
    """
    # Convert the integer to a string
    num_str = str(num)

    # Check if the number is already a palindrome
    if num_str == num_str[::-1]:
        return num

    # Determine the length of the number
    length = len(num_str)

    # If the number has an odd number of digits
    if length % 2 == 1:
        # Get the middle digit
        middle = length // 2
        # Create a new string by taking the first half of the number and reversing it
        new_num_str = num_str[:middle] + num_str[middle:][::-1]
        # Convert the new string back to an integer and return it
        return int(new_num_str)

    # If the number has an even number of digits
    else:
        # Get the first half of the number
        first_half = num_str[:length // 2]
        # Create a new string by taking the first half of the number and reversing it
        new_num_str = first_half + first_half[::-1]
        # Convert the new string back to an integer and return it
        return int(new_num_str)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)