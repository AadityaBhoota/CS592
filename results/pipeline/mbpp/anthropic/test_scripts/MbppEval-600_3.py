def is_Even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def check(candidate):
    assert is_Even(1) == False
    assert is_Even(2) == True
    assert is_Even(3) == False

check(is_Even)