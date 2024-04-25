def find_Rotations(str):
    return len(str) if str * 2 == str * 2 + str else 1

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)