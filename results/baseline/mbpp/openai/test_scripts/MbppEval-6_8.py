def is_Power_Of_Two (x): 
    '''
    Write a python function to check whether the two numbers differ at one bit position only or not.

    Examples:
    differ_At_One_Bit_Pos(13,9) == True
    differ_At_One_Bit_Pos(15,8) == False
    differ_At_One_Bit_Pos(2,4) == False
    '''
def differ_At_One_Bit_Pos(num1, num2):
    # Calculate the XOR of the two numbers
    xor_result = num1 ^ num2
    
    # Count the number of set bits in the XOR result
    count = 0
    while xor_result:
        xor_result &= (xor_result - 1)
        count += 1
    
    # If only one bit is set, return True
    return count == 1

# Test cases




def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )