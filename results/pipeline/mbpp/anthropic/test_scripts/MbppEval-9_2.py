def find_Rotations(s):
    if not s:
        return 0
    
    doubled_s = s + s
    for i in range(1, len(s)):
        if s == doubled_s[i:i+len(s)]:
            return i
    
    return len(s)

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)