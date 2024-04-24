def is_Sum_Of_Powers_Of_Two(n):
    """
    Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.

    Examples:
    is_Sum_Of_Powers_Of_Two(10) == True
    is_Sum_Of_Powers_Of_Two(7) == False
    is_Sum_Of_Powers_Of_Two(14) == True
    """
    # Check if the number is less than 1
    if n < 1:
        return False

    # Convert the number to binary and count the number of set bits
    set_bits = bin(n).count('1')

    # If the number of set bits is equal to 1, it is a power of 2
    return set_bits == 1

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)