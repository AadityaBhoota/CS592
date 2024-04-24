def differ_At_One_Bit_Pos(x, y):
    if x < 0 or y < 0:
        return False
    
    xor_result = x ^ y
    return xor_result & (xor_result - 1) == 0

# Test cases




def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )