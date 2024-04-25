def all_Bits_Set_In_The_Given_Range(n, l, r):
    mask = 0
    for i in range(l, r+1):
        mask |= (1 << i)
    
    return (n & mask) == 0

# Test cases




def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)