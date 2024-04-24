def is_Even(n):
    return n % 2 == 0

# Test cases
assert is_Even(1) == False
assert is_Even(2) == True
assert is_Even(3) == False

def check(candidate):
    assert is_Even(1) == False
    assert is_Even(2) == True
    assert is_Even(3) == False

check(is_Even)