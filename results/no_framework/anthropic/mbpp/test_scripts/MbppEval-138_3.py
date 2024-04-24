def is_Sum_Of_Powers_Of_Two(n):
    """
    Checks whether the given number can be represented as sum of non-zero powers of 2 or not.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number can be represented as sum of non-zero powers of 2, False otherwise.
    """
    if n <= 0:
        return False

    # Convert the number to binary string
    binary_str = bin(n)[2:]

    # Count the number of '1' bits in the binary representation
    num_ones = binary_str.count('1')

    # If the number of '1' bits is less than or equal to 1, it can be represented as sum of non-zero powers of 2
    return num_ones <= 1

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)