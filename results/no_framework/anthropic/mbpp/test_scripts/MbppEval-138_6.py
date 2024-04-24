def is_Sum_Of_Powers_Of_Two(n):
    """
    Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.

    Examples:
    is_Sum_Of_Powers_Of_Two(10) == True
    is_Sum_Of_Powers_Of_Two(7) == False
    is_Sum_Of_Powers_Of_Two(14) == True
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:]
    
    # Check if the binary string contains only '1' characters
    return all(char == '1' for char in binary_str)

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)