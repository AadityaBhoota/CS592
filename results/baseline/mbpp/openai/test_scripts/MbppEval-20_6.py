def is_woodall(x):
    n = 1
    while True:
        woodall_number = n * 2 ** n - 1
        if woodall_number == x:
            return True
        elif woodall_number > x:
            return False
        n += 1

# Test cases




def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)