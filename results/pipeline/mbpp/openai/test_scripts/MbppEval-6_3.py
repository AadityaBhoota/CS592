def is_Power_Of_Two (x): 
    '''
    Write a python function to check whether the two numbers differ at one bit position only or not.

    Examples:
    differ_At_One_Bit_Pos(13,9) == True
    differ_At_One_Bit_Pos(15,8) == False
    differ_At_One_Bit_Pos(2,4) == False
    '''
def is_Power_Of_Two(x, y):
    binary_x = bin(x)[2:]
    binary_y = bin(y)[2:]
    
    differing_bit_count = 0
    differing_bit_position = -1
    
    for i, (bit_x, bit_y) in enumerate(zip(binary_x[::-1], binary_y[::-1])):
        if bit_x != bit_y:
            differing_bit_count += 1
            differing_bit_position = i
    
    return differing_bit_count == 1

def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )