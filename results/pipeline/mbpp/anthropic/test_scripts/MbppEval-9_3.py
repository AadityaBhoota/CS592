def find_Rotations(str):
    min_rotations = len(str)
    for i in range(1, len(str)):
        rotated_str = str[i:] + str[:i]
        if rotated_str == str:
            min_rotations = i + 1
            break
    return min_rotations

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)