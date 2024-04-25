def all_Bits_Set_In_The_Given_Range(n, l, r):
    binary_n = bin(n)[2:]
    
    for i in range(l-1, r):
        if i < len(binary_n) and binary_n[-i-1] == '1':
            return False
    
    return True

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)