def all_Bits_Set_In_The_Given_Range(n, l, r):
    """
    Write a python function to check whether all the bits are set in the given range or not.

    Examples:
    all_Bits_Set_In_The_Given_Range(4, 1, 2) == True
    all_Bits_Set_In_The_Given_Range(17, 2, 4) == True
    all_Bits_Set_In_The_Given_Range(39, 4, 6) == False
    """
    # Create a mask with all bits set in the given range
    mask = (1 << (r - l + 1)) - 1
    mask <<= (l - 1)

    # Check if the bits in the given range are all set
    return (n & mask) == mask

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)