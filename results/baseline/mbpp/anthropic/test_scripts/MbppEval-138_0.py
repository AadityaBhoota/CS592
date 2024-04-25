def is_Sum_Of_Powers_Of_Two(n):
    """
    Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.

    Examples:
    is_Sum_Of_Powers_Of_Two(10) == True
    is_Sum_Of_Powers_Of_Two(7) == False
    is_Sum_Of_Powers_Of_Two(14) == True
    """
    if n < 1:
        return False

    binary_representation = bin(n)[2:]  # Convert n to binary string and remove '0b' prefix
    return all(digit == '1' for digit in binary_representation)

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)