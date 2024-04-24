def tuple_to_int(nums):
    """
    Convert a given tuple of positive integers into a single integer.

    Args:
        nums (tuple): A tuple of positive integers.

    Returns:
        int: The single integer formed by concatenating the digits in the tuple.
    """
    # Convert the tuple to a string
    num_str = ''.join(str(digit) for digit in nums)
    
    # Convert the string back to an integer
    return int(num_str)

def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567

check(tuple_to_int)