def differ_At_One_Bit_Pos(x, y):
    # Count the number of differing bits
    xor_result = x ^ y
    count = 0
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1
    
    # Check if only one bit position differs
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