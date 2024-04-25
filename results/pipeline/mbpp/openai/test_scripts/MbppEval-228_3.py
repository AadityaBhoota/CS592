def all_Bits_Set_In_The_Given_Range(n, l, r):
    bits_in_range = get_bits_in_range(n, l, r)
    return bits_in_range == 0

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)