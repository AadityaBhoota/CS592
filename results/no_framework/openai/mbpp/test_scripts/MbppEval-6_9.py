def differ_At_One_Bit_Pos(x, y):
    '''
    Check whether the two numbers differ at one bit position only.

    Args:
    x, y: Integers to compare

    Returns:
    True if the numbers differ at one bit position, False otherwise
    '''
    # XOR the two numbers to find the differing bits
    xor_result = x ^ y
    
    # If the result is a power of 2, it means only one bit position is different
    return xor_result & (xor_result - 1) == 0

# Test the function with the given examples




def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )