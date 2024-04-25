def all_Bits_Set_In_The_Given_Range(n, l, r):
    """
    Write a Python function to check whether all the bits are set in the given range or not.

    Examples:
    all_Bits_Set_In_The_Given_Range(4, 1, 2) == True
    all_Bits_Set_In_The_Given_Range(17, 2, 4) == True
    all_Bits_Set_In_The_Given_Range(39, 4, 6) == False
    """
    # Convert the number to its binary representation
    binary_str = bin(n)[2:]

    # Check if all the bits in the given range are set
    for i in range(l - 1, r):
        if binary_str[i] == '0':
            return False

    return True

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)