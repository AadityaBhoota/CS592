def find_Rotations(s):
    rotations = 0
    temp_str = s + s
    
    for i in range(len(s)):
        if s == temp_str[i:i+len(s)]:
            return rotations
        rotations += 1
    
    return len(s)

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)