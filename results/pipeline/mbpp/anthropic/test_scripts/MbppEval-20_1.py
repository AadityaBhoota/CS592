def is_woodall(x):
    woodall_number = 2 ** x + 1
    return woodall_number == x

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)