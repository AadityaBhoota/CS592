def find_Rotations(s):
    n = len(s)
    if n == 0:
        return 0
    
    # Concatenate the string with itself to find the minimum rotation
    double_s = s + s
    
    # Use Rabin-Karp algorithm to find the first occurrence of the original string in the doubled string
    for i in range(1, n):
        if s == double_s[i:i+n]:
            return i
    
    # If no rotation is found, the string is already the minimum rotation
    return n

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)