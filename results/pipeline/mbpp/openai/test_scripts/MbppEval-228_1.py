def all_Bits_Set_In_The_Given_Range(n, l, r):
    binary_representation = bin(n)[2:]
    
    for i in range(l, r+1):
        if len(binary_representation) < i or binary_representation[-i] != '1':
            return False

    return True

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)