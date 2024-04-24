def find_Rotations(input_str):
    n = len(input_str)
    for i in range(1, n+1):
        if n % i == 0:
            substr = input_str[:i]
            rotations = input_str.count(substr)
            if rotations * i == n:
                return n // i
    return n

# Test cases




def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)