def find_Rotations(s):
    n = len(s)
    for i in range(1, n):
        if n % i == 0:
            substring = s[:i]
            if substring * (n // i) == s:
                return n // i
    return n

# Test cases




def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)