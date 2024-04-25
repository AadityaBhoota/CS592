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
    Write a python function to check whether the two numbers differ at one bit position only or not.

    Examples:
    differ_At_One_Bit_Pos(13, 9) == True
    differ_At_One_Bit_Pos(15, 8) == False
    differ_At_One_Bit_Pos(2, 4) == False
    """
    # Convert the numbers to their binary representations
    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]

    # Ensure both numbers have the same number of bits
    max_len = max(len(x_bin), len(y_bin))
    x_bin = x_bin.zfill(max_len)
    y_bin = y_bin.zfill(max_len)

    # Count the number of bit positions where the numbers differ
    diff_count = 0
    for i in range(max_len):
        if x_bin[i] != y_bin[i]:
            diff_count += 1

    # Return True if the numbers differ at one bit position only, False otherwise
    return diff_count == 1

def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )