def all_Bits_Set_In_The_Given_Range(n, l, r):
    mask = (1 << (r - l + 1)) - 1
    mask = mask << (l - 1)
    return n & mask == 0

# Test cases




def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)