def is_Sum_Of_Powers_Of_Two(n):
    """
    Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.

    Examples:
    is_Sum_Of_Powers_Of_Two(10) == True
    is_Sum_Of_Powers_Of_Two(7) == False
    is_Sum_Of_Powers_Of_Two(14) == True
    """
    if n == 0:
        return False

    bin_rep = bin(n)[2:]  # Convert the number to binary representation and remove the '0b' prefix
    ones_count = bin_rep.count('1')

    return ones_count == len(bin_rep)

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)