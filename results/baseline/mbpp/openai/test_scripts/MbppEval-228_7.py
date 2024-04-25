def all_Bits_Set_In_The_Given_Range(n, l, r):
    for i in range(l, r+1):
        if n & (1 << i):
            return False
    return True

# Test cases
assert all_Bits_Set_In_The_Given_Range(4, 1, 2) == True
assert all_Bits_Set_In_The_Given_Range(17, 2, 4) == True
assert all_Bits_Set_In_The_Given_Range(39, 4, 6) == False

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)