def is_Sum_Of_Powers_Of_Two(n):
    """
    Checks whether the given number can be represented as a sum of non-zero powers of 2.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number can be represented as a sum of non-zero powers of 2, False otherwise.
    """
    binary_repr = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
    
    # Check if the binary representation has only non-zero digits
    return all(int(digit) > 0 for digit in binary_repr)

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)