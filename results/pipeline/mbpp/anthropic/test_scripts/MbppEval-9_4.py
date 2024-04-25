def find_Rotations(str):
    doubled_str = str + str
    index = doubled_str.find(str)
    return len(str) - index

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)