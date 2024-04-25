def is_Power_Of_Two (x): 
    '''
    Write a python function to check whether the two numbers differ at one bit position only or not.

    Examples:
    differ_At_One_Bit_Pos(13,9) == True
    differ_At_One_Bit_Pos(15,8) == False
    differ_At_One_Bit_Pos(2,4) == False
    '''
def differ_At_One_Bit_Pos(x, y):
    """
    Check whether the two numbers differ at one bit position only.
    
    Args:
        x (int): The first number.
        y (int): The second number.
    
    Returns:
        bool: True if the numbers differ at one bit position only, False otherwise.
    """
    xor_result = x ^ y
    set_bits = bin(xor_result).count('1')
    return set_bits == 1

def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )