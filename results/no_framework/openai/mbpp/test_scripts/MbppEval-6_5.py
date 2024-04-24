def differ_At_One_Bit_Pos(num1, num2):
    # Count the number of bits that are different between num1 and num2
    count = num1 ^ num2
    bit_count = 0
    while count:
        count &= (count - 1)
        bit_count += 1

    # Return True if only one bit is different
    return bit_count == 1

# Testing the function with the given examples




def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )