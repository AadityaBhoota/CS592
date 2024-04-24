def dif_Square(n):
    """
    Checks whether the given number can be represented as the difference of two squares or not.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number can be represented as the difference of two squares, False otherwise.
    """
    # Check if the number is a perfect square
    for i in range(int(n ** 0.5) + 1):
        if i * i == n:
            return True
    
    # Check if the number can be represented as the difference of two squares
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(i + 1, int(n ** 0.5) + 1):
            if i * i - j * j == n:
                return True
    
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)