def find_Rotations(str): 
    n = len(str)
    for i in range(1, n):
        rotated_str = str[i:] + str[:i]
        if rotated_str == str:
            return i
    return -1

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)