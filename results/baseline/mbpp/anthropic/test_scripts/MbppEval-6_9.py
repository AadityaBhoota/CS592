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
    Checks whether the two numbers differ at one bit position only.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        bool: True if the two numbers differ at one bit position only, False otherwise.
    """
    # Calculate the XOR of the two numbers
    diff = x ^ y

    # Check if the XOR has exactly one set bit
    return diff != 0 and (diff & (diff - 1)) == 0

def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )