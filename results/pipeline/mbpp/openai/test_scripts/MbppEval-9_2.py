def find_Rotations(input_str):
    str_len = len(input_str)

    if str_len < 2:
        return 0
    
    for i in range(1, str_len):
        rotated_str = input_str[i:] + input_str[:i]
        if input_str == rotated_str:
            return i

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)