def differ_At_One_Bit_Pos(x, y):
    """
    Check whether the two numbers differ at one bit position only or not.

    Args:
        x (int): First number.
        y (int): Second number.

    Returns:
        bool: True if the two numbers differ at one bit position only, False otherwise.
    """
    # Use XOR to find the bit positions where the two numbers differ
    diff = x ^ y

    # Check if the number of set bits (1s) in the difference is exactly 1
    return bin(diff).count('1') == 1

def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )