def is_Sum_Of_Powers_Of_Two(n):
    """
    Checks whether the given number can be represented as a sum of non-zero powers of 2.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number can be represented as a sum of non-zero powers of 2, False otherwise.
    """
    # Convert the number to binary representation
    binary_n = bin(n)[2:]

    # Check if the binary representation contains only '1' characters
    return all(char == '1' for char in binary_n)

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)