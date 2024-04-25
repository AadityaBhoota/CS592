def is_Sum_Of_Powers_Of_Two(n):
    """
    Checks whether the given number can be represented as a sum of non-zero powers of 2.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number can be represented as a sum of non-zero powers of 2, False otherwise.
    """
    if n <= 0:
        return False
    
    # Convert the number to binary and count the number of '1' bits
    binary_count = bin(n).count('1')
    
    # If the number of '1' bits is equal to 1, the number is a power of 2
    # If the number of '1' bits is greater than 1, the number can be represented as a sum of non-zero powers of 2
    return binary_count > 1

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)