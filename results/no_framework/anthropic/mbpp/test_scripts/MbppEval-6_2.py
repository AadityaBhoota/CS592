def differ_At_One_Bit_Pos(num1, num2):
    """
    Checks whether two numbers differ at one bit position only.
    
    Args:
        num1 (int): First number.
        num2 (int): Second number.
    
    Returns:
        bool: True if the numbers differ at one bit position only, False otherwise.
    """
    # Calculate the XOR of the two numbers
    xor_result = num1 ^ num2
    
    # Check if the XOR result has exactly one bit set
    return bin(xor_result).count('1') == 1

def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )