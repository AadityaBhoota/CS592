def find_Rotations(str): 
    if len(str) <= 1:
        return 0
    
    rotations = [str[i:] + str[:i] for i in range(len(str))]
    
    for idx, rotation in enumerate(rotations):
        if rotation == str:
            return idx + 1

    return 0

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)