def find_Rotations(str): 
    for i in range(1, len(str) + 1):
        if str == str[:i] * (len(str) // i):
            return len(str) // i
    return len(str)

# Test Cases




def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)