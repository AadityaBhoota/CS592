def find_Rotations(s):
    # Function to check if a given rotation forms the same string
    def isSameString(rotation, s):
        return rotation == s
    
    n = len(s)
    
    for i in range(1, n+1):
        if n % i == 0:
            rotation = s[i:] + s[:i]
            if isSameString(rotation, s):
                return i
    
    return n

# Test cases




def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)